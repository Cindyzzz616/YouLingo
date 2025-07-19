from moviepy import VideoFileClip
import whisper

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
        self.transcript_text = self.transcript['text']
        self.word_list = self.transcript_text.strip().split()
        self.word_count = len(self.word_list)
        self.audio_path = self.extract_audio()
        self.wpm = self.calculate_wpm()
        self.spm = self.calculate_spm()
        # TODO could also calculate average syllables/word, etc.

    def __str__(self):
        transcript_preview = self.transcript["text"][:100] + "..." if self.transcript and "text" in self.transcript else "No transcript"
        return (
            f"🎬 Video(path='{self.path}')\n"
            f"📝 Transcript Preview: {transcript_preview}\n"
            f"⏱️ Total Length: {self.length:.2f} seconds\n"
            f"🗣️ Speech Length: {self.speech_length:.2f} seconds\n"
            f"🎤 Audio Path: {self.audio_path}\n"
            f"🕒 Words Per Minute: {self.wpm:.2f} WPM"
            f"\n📖 Word Count: {self.word_count}\n"
            f"🗣️ Syllables Per Minute: {self.spm:.2f} SPM"
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
        model = whisper.load_model("base")  # or "small", "medium", "large"
        result = model.transcribe(self.path)
        return result
    
    def extract_audio(self):
        """
        Extract audio from the video and save it to the specified path. Return the path of the saved audio file.
        """
        video = VideoFileClip(self.path)
        audio = video.audio
        audio_path = self.path.replace(".MP4", "_audio.wav")
        audio.write_audiofile(audio_path)
        return audio_path
    
    def calculate_speech_length(self) -> float:
        """
        Calculate the total speech length in seconds from the transcript.
        """
        total_duration = 0.0
        for segment in self.transcript["segments"]:
            start = segment["start"]
            end = segment["end"]
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
