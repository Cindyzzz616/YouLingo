import os
from xml.parsers.expat import model
from moviepy import VideoFileClip
import whisper
from faster_whisper import WhisperModel
from VAT import compute_ptrs_from_audio
# TODO don't forget you can export the whisper output as a subtitle .srt file
from nltk.corpus import cmudict

# Load CMU dict
d = cmudict.dict()

def count_syllables(word: str) -> int:
    word = word.lower()
    if word in d:
        # Some words have multiple pronunciations — take the first one
        return max([len([phoneme for phoneme in pron if phoneme[-1].isdigit()])
                    for pron in d[word]])
    else:
        # Fallback: estimate based on vowels
        return estimate_syllables_fallback(word)

def estimate_syllables_fallback(word: str) -> int:
    # Very rough fallback: count vowel groups
    import re
    return len(re.findall(r"[aeiouy]+", word.lower()))

class Video:
    """
    Represents a video file with its path.
    """

    path: str
    length: float = -1.0  # Default value indicating length is unknown
    audio_path: str = ""  # Default value for audio extraction path
    wpm: float = -1.0  # Default value for speech rate in words per minute

    def __init__(self, path: str):
        self.path = path
        self.transcript = self.transcribe()
        self.length = self.calculate_length()
        self.speech_length = self.calculate_speech_length()
        self.transcript_text = self.get_full_transcript()
        self.word_list = self.transcript_text.strip().split()
        self.word_count = len(self.word_list)
        self.audio_path = self.extract_audio()
        self.wpm = self.calculate_wpm()
        self.spm = self.calculate_spm()
        self.average_ptr = compute_ptrs_from_audio(self.audio_path)
        # TODO could also calculate average syllables/word, etc.

    def __str__(self):
        return (
            f"🎬 Video(path='{self.path}')\n"
            f"📝 Transcript Preview: {self.transcript_text}\n"
            f"⏱️ Total Length: {self.length:.2f} seconds\n"
            f"🗣️ Speech Length: {self.speech_length:.2f} seconds\n"
            f"🎤 Audio Path: {self.audio_path}\n"
            f"🕒 Words Per Minute: {self.wpm:.2f} WPM\n"
            f"📖 Word Count: {self.word_count}\n"
            f"🗣️ Syllables Per Minute: {self.spm:.2f} SPM\n"
            f"📊 Average PTR: {self.average_ptr:.3f}"
        )
    
    def calculate_length(self) -> float:
        """
        Calculate the length of the video in seconds.
        """
        clip = VideoFileClip(self.path)
        return clip.duration  # in seconds

    def transcribe(self):
        """
        Transcribe the audio of the video using Whisper ASR.
        """
        model = WhisperModel("base", compute_type="float32")
        segments, info = model.transcribe(self.path)
        return {"segments": list(segments), "info": info}
    
    def get_full_transcript(self) -> str:
        """
        Get the full transcript text from the transcription segments.
        """
        full_text = " ".join([segment.text for segment in self.transcript["segments"]])
        return full_text

    def extract_audio(self):
        # Get base filename without extension
        base_filename = os.path.basename(self.path).replace(".MP4", "_audio.wav")

        # Define output directory and full path
        output_dir = "video_analysis/audios"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, base_filename)

        # Extract and write audio
        audio = VideoFileClip(self.path).audio
        audio.write_audiofile(output_path)

        return output_path
    
    def calculate_speech_length(self) -> float:
        """
        Calculate the total speech length in seconds from the transcript.
        """
        total_duration = 0.0
        for segment in self.transcript["segments"]:
            start = segment.start
            end = segment.end
            total_duration += (end - start)
        return total_duration

    def calculate_wpm(self) -> float:
        """
        Calculate the speech rate in words per minute (WPM).
        """

        wps = self.word_count / self.speech_length if self.speech_length > 0 else 0
        wpm = wps * 60

        return wpm

    def calculate_spm(self) -> float:
        """
        Calculate the speech rate in syllables per minute (SPM).
        """
        total_syllables = 0
        for word in self.word_list:
            syllable_count = count_syllables(word)
            total_syllables += syllable_count

        sps = total_syllables / self.speech_length if self.speech_length > 0 else 0
        spm = sps * 60

        return spm

# def compute_ptr_per_segment(self, pause_threshold=0.3):

#     model = WhisperModel("base", compute_type="int8")  # or "medium", "large"

#     segments, _ = model.transcribe(self.audio_path, word_timestamps=True)

#     for segment in segments:
#         print(segment.start, segment.end, segment.text)
#         for word in segment.words:
#             print(f"  {word.word} ({word.start:.4f} - {word.end:.4f})")

#     results = []
#     segments = self.transcript["segments"]

#     for seg in segments:
#         total_duration = seg["end"] - seg["start"]
#         words = seg.get("words", [])
#         speaking_time = 0.0

#         if not words or total_duration <= 0:
#             results.append({
#                 "text": seg["text"],
#                 "duration": total_duration,
#                 "PTR": 0.0
#             })
#             continue

#         # Add durations of all words
#         for i in range(len(words)):
#             word_duration = words[i]["end"] - words[i]["start"]
#             speaking_time += word_duration

#             # If this isn't the last word, check for pause
#             if i < len(words) - 1:
#                 gap = words[i+1]["start"] - words[i]["end"]
#                 if gap > pause_threshold:
#                     pass  # pause time excluded from speaking time

#         ptr = speaking_time / total_duration if total_duration > 0 else 0.0
#         results.append({
#             "text": seg["text"],
#             "duration": round(total_duration, 2),
#             "speaking_time": round(speaking_time, 2),
#             "PTR": round(ptr, 2)
#         })

#     return results