# TODO should I change the data structure of words so they contain all their relevant info? Like syntactic category, frequency, etc
# so like having a Word object
# TODO don't forget you can export the whisper output as a subtitle .srt file


import os
import re
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from moviepy import VideoFileClip
from faster_whisper import WhisperModel

from Word import Word
from VAT import preprocess_audio
from VAT import get_voiced_intervals_webrtcvad
from diarization import diarize
from external_data.contractions import CONTRACTIONS

# Unused imports
# from xml.parsers.expat import model
# import whisper
# from VAT import compute_ptrs_from_audio

##### Preparing various packages #####

# Loading the phoneme inventory database
phoneme_database = pd.read_csv(
    "https://raw.githubusercontent.com/phoible/dev/master/data/phoible.csv",
    low_memory=False
)

##### The actual Video object #####

class Video:
    """
    Represents a video file with its path.
    All attributes are properties of the video ONLY (not dependent on any users)
    """

    # TODO need to double check type contracts
    path: str
    audio_path: str
    length: float = -1.0  # Default value indicating length is unknown
    audio_path: str = ""  # Default value for audio extraction path
    wpm: float = -1.0  # Default value for speech rate in words per minute
    tokens: list[Word]

    def __init__(self, path: str, audio_folder: str):
        # File paths
        self.path = path # the video path
        self.audio_path = self.extract_audio(audio_folder)

        # Transcript attributes
        self.transcript = self.transcribe() # a transcript object from Whisper
        self.transcript_text = self.get_full_transcript()
        self.language = self.get_language()
        self.number_of_speakers = diarize(self.audio_path)

        # Length attributes
        self.length = self.calculate_length()
        self.vad_duration = self.calculate_speech_length()[0] # duration of voice activation detection
        self.total_segment_length = self.calculate_speech_length()[1] # duration of all transcript segments/sentences

        if self.language != 'en':
            # Lexical attributes
            self.tokens = []
            self.types = {}
            self.word_count = -1

            # Phonological attributes
            self.wpm = -1
            self.spm = -1
            self.average_ptr = -1
        else:
            # Lexical attributes
            self.tokens = self.get_tokens()
            self.types = self.get_set()
            self.word_count = len(self.tokens)

            # Phonological attributes
            self.wpm = self.calculate_wpm() # words per minute
            self.spm = self.calculate_spm() # syllables per minute
            self.average_ptr = self.voiced_slices_for_segments()

    def __str__(self):
        return (
            f"🎬 Video path: {self.path}\n"
            f"🎤 Audio Path: {self.audio_path}\n"
            f"📝 Transcript Preview: {self.transcript_text}\n"
            f"🌏 Language: {self.language}\n"
            f"👫 Number of speakers: {self.number_of_speakers}\n"
            f"⏱️ Total Length: {self.length:.2f} seconds\n"
            f"🗣️ VAD duration: {self.vad_duration:.2f} seconds\n"
            f"💬 Total segment length: {self.total_segment_length:.2f} seconds\n"
            f"Lexical properties:\n"            
            f"📖 Word Count: {self.word_count} words\n"
            f"Phonological properties:\n"
            f"🕒 Words Per Minute: {self.wpm:.2f} WPM\n"
            f"🗣️ Syllables Per Minute: {self.spm:.2f} SPM\n"
            f"📊 Average PTR: {self.average_ptr:.2f}\n"
        )
    
    # def extract_audio(self, audio_folder: str):
    #     # Get base filename without extension
    #     base_filename = os.path.basename(self.path).replace(".MP4", "_audio.wav")

    #     # Define output directory and full path
    #     output_dir = audio_folder
    #     os.makedirs(output_dir, exist_ok=True)
    #     output_path = os.path.join(output_dir, base_filename)

    #     # Extract and write audio
    #     audio = VideoFileClip(self.path).audio
    #     audio.write_audiofile(output_path)

    #     return output_path
    
    def extract_audio(self, audio_folder: str):
        # Ensure output directory exists
        output_dir = Path(audio_folder)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Build audio file name (preserve stem, change extension)
        output_path = output_dir / f"{Path(self.path).stem}_audio.wav"

        # Extract audio and save
        with VideoFileClip(self.path) as video:
            video.audio.write_audiofile(str(output_path))

        return str(output_path)
    
    def transcribe(self):
        """
        Transcribe the audio of the video using Whisper ASR.
        """
        model = WhisperModel("base", compute_type="float32")
        segments, info = model.transcribe(self.path, 
                                          vad_filter=True,
                                          multilingual=True,
                                          language_detection_segments=10) # NOTE can set multilingual=True here
        return {"segments": list(segments), "info": info}
    
    def get_full_transcript(self) -> str:
        """
        Get the full transcript text from the transcription segments.
        """
        full_text = " ".join([segment.text for segment in self.transcript["segments"]])
        return full_text
    
    def get_language(self) -> str:
        return self.transcript["info"].language
    
    def calculate_length(self) -> float:
        """
        Calculate the length of the video in seconds.
        """
        clip = VideoFileClip(self.path)
        return clip.duration  # in seconds
    
    def calculate_speech_length(self):
        """
        Calculate the total speech length in seconds from the transcript.
        """

        # The old way of calculating speech length: subtracting duration of all sentences from total duration of video
        total_duration = 0.0
        for segment in self.transcript["segments"]:
            start = segment.start
            end = segment.end
            total_duration += (end - start)
        return self.transcript["info"].duration_after_vad, total_duration
    
    def get_tokens(self) -> list[Word]:
        """
        Get a list of words (tokens) from the transcript. Repeated words are counted as different tokens.
        """
        word_tokens = []
        # Split on any sequence of whitespace or punctuation
        tokens = re.split(r"[^\w']+", self.transcript_text)

        # Expland contractions
        for token in tokens:
            for key in CONTRACTIONS.keys():
                if token.lower() == key.lower():
                    tokens.extend(CONTRACTIONS[key])
                    tokens.remove(token)
        
        # Remove possessives after contractions are handled
        for token in tokens:
            if token.endswith("'s"):
                token.removesuffix("'s")

        # Remove empty strings
        tokens = [t for t in tokens if t]

        # Convert tokens to Word objects
        for token in tokens:
            word_tokens.append(Word(token))

        return word_tokens
    
    def get_set(self):
        word_set_flattened = set()
        for token in self.tokens:
            if token.text.lower() not in word_set_flattened:
                word_set_flattened.add(token.text.lower())
        word_set = set()
        for word in word_set_flattened:
            word_set.add(Word(word))
        return word_set
    
    def compute_word_frequency_average(self):
        """
        Compute the average frequency of words in the transcript.
        Returns the average frequency as a float.
        """
        frequencies = []
        total_words_in_corpus = len(self.tokens)
        for token in self.tokens:
            if token.frequency < 0:
                total_words_in_corpus -= 1
            else:
                frequencies.append(token.frequency)
        
        if not frequencies:
            return 0.0, 0.0
        average_freq = sum(frequencies) / total_words_in_corpus
        variance = sum((freq - average_freq) ** 2 for freq in frequencies) / total_words_in_corpus

        return average_freq, variance

    def calculate_wpm(self) -> float:
        """
        Calculate the speech rate in words per minute (WPM).
        """

        wps = self.word_count / self.vad_duration if self.vad_duration > 0 else 0
        wpm = wps * 60

        return wpm

    def calculate_spm(self) -> float:
        """
        Calculate the speech rate in syllables per minute (SPM).
        """
        total_syllables = 0
        for word in self.tokens:
            total_syllables += word.syllable_count

        sps = total_syllables / self.vad_duration if self.vad_duration > 0 else 0
        spm = sps * 60

        return spm
    
    def voiced_slices_for_segments(self, eps: float = 1e-6):
        """
        For each segment, return the list of voiced sub-intervals within it,
        plus the segment's PTR (voiced_time / duration).
        """
        results = []
        preprocessed_path = preprocess_audio(self.audio_path)
        voiced = get_voiced_intervals_webrtcvad(preprocessed_path)
        voiced = sorted(voiced)  # ensure order
        segments = self.transcript["segments"]

        for seg in segments:
            s0 = seg.start
            s1 = seg.end
            text = seg.text

            dur = max(0.0, s1 - s0)
            if dur <= eps:
                results.append({
                    "start": s0, "end": s1, "text": text,
                    "voiced_intervals": [], "voiced_time": 0.0, "ptr": 0.0
                })
                continue

            # collect overlaps
            overlaps = []
            voiced_time = 0.0

            # iterate only over voiced intervals that can intersect [s0, s1]
            # (early break once v_start >= s1)
            for v_start, v_end in voiced:
                if v_end <= s0 + eps:
                    continue
                if v_start >= s1 - eps:
                    break
                a = max(s0, v_start)
                b = min(s1, v_end)
                if b - a > eps:
                    overlaps.append((a, b))
                    voiced_time += (b - a)

            ptr = voiced_time / dur if dur > 0 else 0.0

            results.append({
                "start": s0,
                "end": s1,
                "text": text,
                "voiced_intervals": overlaps,
                "voiced_time": round(voiced_time, 6),
                "ptr": round(ptr, 6),
            })
            # print(voiced, "\n")
            # print(segments, "\n")
            # print(results, "\n")

            total_ptr = 0
            total_segs = len(results)
            for seg in results:
                if seg["ptr"] > 0:
                    total_ptr += seg["ptr"]
                else:
                    total_segs -= 1
            avg_ptr = total_ptr / total_segs

        return avg_ptr

    # def compute_ptr(self):
    #     preprocessed_path = preprocess_audio(self.audio_path)
    #     voiced_intervals = get_voiced_intervals_webrtcvad(preprocessed_path)
    #     for segment in self.transcript["segments"]: 
    #         i = 0
    #         while i < len(voiced_intervals) - 1:
    #             this_interval = voiced_intervals[i]
    #             next_interval = voiced_intervals[i+1]
    #             this_end = this_interval[1]
    #             next_start = next_interval[0]
    #     return 0
    
##### Example usage #####

if __name__ == "__main__":
    # Example usage
    video = Video(path="video_analysis/videos/etymology.MP4", audio_folder="video_analysis/audios")
    print(video)
    for token in video.tokens:
        print(token.text)
    print("\n")
    for type in video.types:
        print(type.text)

    # print(video.transcript["info"], "\n")
    # print(video.transcript["info"].duration, type(video.transcript["info"].duration))
    # print(video.transcript["info"].duration_after_vad, type(video.transcript["info"].duration_after_vad))

    # NOTE there is a multilingual=FALSE attribute in transcription info
    # NOTE it's pretty bad with code-switching though

    # # Plot a histogram with word frequencies
    # frequencies = []
    # for token in video.tokens:
    #     if token.frequency > 0:
    #         frequencies.append(token.frequency)
    # plt.hist(frequencies, bins=100, edgecolor='black', align='left')
    # plt.xlabel('Word Frequency')
    # plt.ylabel('Number of Unique Words')
    # plt.title('Distribution of Word Frequencies')
    # # plt.xticks(range(1, max(frequencies)+1))  # Show integer ticks
    # plt.show()



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