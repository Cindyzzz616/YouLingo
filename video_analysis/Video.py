# TODO should I change the data structure of words so they contain all their relevant info? Like syntactic category, frequency, etc
# so like having a Word object
# TODO don't forget you can export the whisper output as a subtitle .srt file


import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from moviepy import VideoFileClip
from faster_whisper import WhisperModel

from Word import Word
from VAT import compute_ptrs_from_audio

# Unused imports
# from xml.parsers.expat import model
# import whisper

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

    def __init__(self, path: str):
        # File paths
        self.path = path # the video path
        self.audio_path = self.extract_audio()

        # Transcript attributes
        self.transcript = self.transcribe() # a transcript object from Whisper
        self.transcript_text = self.get_full_transcript()

        # Length attributes
        self.length = self.calculate_length()
        self.speech_length = self.calculate_speech_length() # a rougher estimate of the amount of time where there's articulation

        # Lexical attributes
        self.tokens = self.get_tokens()
        self.types = set(self.tokens)
        self.word_count = len(self.tokens)

        # Phonological attributes
        self.wpm = self.calculate_wpm() # words per minute
        self.spm = self.calculate_spm() # syllables per minute
        self.average_ptr = compute_ptrs_from_audio(self.audio_path) # TODO this is NOT correct bc this only has pauses between sentences

    def __str__(self):
        return (
            f"🎬 Video(path='{self.path}')\n"
            f"🎤 Audio Path: {self.audio_path}\n"
            f"📝 Transcript Preview: {self.transcript_text}\n"
            f"⏱️ Total Length: {self.length:.2f} seconds\n"
            f"🗣️ Speech Length: {self.speech_length:.2f} seconds\n"
            f"Lexical properties:\n"            
            f"📖 Word Count: {self.word_count} words\n"
            f"Phonological properties:\n"
            f"🕒 Words Per Minute: {self.wpm:.2f} WPM\n"
            f"🗣️ Syllables Per Minute: {self.spm:.2f} SPM\n"
            f"📊 Average PTR: {self.average_ptr:.3f}\n"
        )
    
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

    def calculate_length(self) -> float:
        """
        Calculate the length of the video in seconds.
        """
        clip = VideoFileClip(self.path)
        return clip.duration  # in seconds
    
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
    
    def get_tokens(self) -> list:
        """
        Get a list of words (tokens) from the transcript. Repeated words are counted as different tokens.
        """
        word_tokens = []
        # Split on any sequence of whitespace or punctuation
        tokens = re.split(r"[^\w']+", self.transcript_text)

        # Remove empty strings
        tokens = [t for t in tokens if t]

        # Convert tokens to Word objects
        for token in tokens:
            word_tokens.append(Word(token))

        return word_tokens
    
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

        wps = self.word_count / self.speech_length if self.speech_length > 0 else 0
        wpm = wps * 60

        return wpm

    def calculate_spm(self) -> float:
        """
        Calculate the speech rate in syllables per minute (SPM).
        """
        total_syllables = 0
        for word in self.tokens:
            total_syllables += word.syllable_count

        sps = total_syllables / self.speech_length if self.speech_length > 0 else 0
        spm = sps * 60

        return spm
    
##### Example usage #####

if __name__ == "__main__":
    # Example usage
    video = Video(path="video_analysis/videos/linguistic_intelligence.MP4")
    print(video)

    # Plot a histogram with word frequencies
    frequencies = []
    for token in video.tokens:
        if token.frequency > 0:
            frequencies.append(token.frequency)
    plt.hist(frequencies, bins=100, edgecolor='black', align='left')
    plt.xlabel('Word Frequency')
    plt.ylabel('Number of Unique Words')
    plt.title('Distribution of Word Frequencies')
    # plt.xticks(range(1, max(frequencies)+1))  # Show integer ticks
    plt.show()



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