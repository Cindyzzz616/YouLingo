import os
import re
# from xml.parsers.expat import model
import pandas as pd
import matplotlib.pyplot as plt
from moviepy import VideoFileClip
import whisper
from faster_whisper import WhisperModel
from VAT import compute_ptrs_from_audio
# TODO don't forget you can export the whisper output as a subtitle .srt file
from nltk.corpus import cmudict
from g2p_en import G2p
from arpa_to_ipa_map import arpabet_to_ipa_map

# Load the frequency dictionary
freq_dict = pd.read_csv("video_analysis/SUBTLEXus74286wordstextversion.txt", sep='\t')

# g2p contains info on lexical stress!
# example usage:
g2p = G2p()
phonemes = g2p("The elephant is big. You're Tara's friend! My friend's name is chief-inspector, or father in law.")
print(phonemes)
# Output: ['DH', 'AH0', ' ', 'EH1', 'L', 'AH0', 'F', 'AH0', 'N', 'T', ' ', 'IH1', 'Z', ' ', 'B', 'IH1', 'G', '.']

# Load the phoneme inventory database
phoneme_database = pd.read_csv(
    "https://raw.githubusercontent.com/phoible/dev/master/data/phoible.csv",
    low_memory=False
)

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
        self.word_list = self.get_word_list()
        self.word_count = len(self.word_list)
        self.phoneme_list = self.get_phoneme_list()
        self.audio_path = self.extract_audio()
        self.wpm = self.calculate_wpm()
        self.spm = self.calculate_spm()
        self.average_ptr = compute_ptrs_from_audio(self.audio_path)
        self.word_list_frequency = self.compute_word_list_frequency()
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
            f"📊 Average PTR: {self.average_ptr:.3f}\n"
            f"🔡 Phoneme List: {self.phoneme_list}"
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
    
    def get_word_list(self) -> list:
        """
        Get a list of words from the transcript.
        """
        # Split on any sequence of whitespace or punctuation
        tokens = re.split(r"[^\w']+", self.transcript_text)

        # Remove empty strings
        tokens = [t for t in tokens if t]
        return tokens

    def get_phoneme_list(self) -> list:
        """
        Get a list of phonemes of each word from the transcript. Convert each phoneme from ARPAbet to IPA.
        """
        phoneme_list = []
        for word in self.word_list:
            # Get a list of ARPAbet phonemes in a word
            arpabet_phonemes = g2p(word)

            # Convert ARPAbet to IPA
            ipa_phonemes = []
            for phoneme in arpabet_phonemes:
                # Handle stress markers if they are attached to vowels (e.g., AE1)
                if len(phoneme) > 1 and phoneme[-1].isdigit():
                    base_phoneme = phoneme[:-1]
                    # TODO handle stress markers
                    # stress_marker = phoneme[-1]
                    if base_phoneme in arpabet_to_ipa_map:
                        # ipa_phonemes.append(arpabet_to_ipa_map[stress_marker] + arpabet_to_ipa_map[base_phoneme])
                        ipa_phonemes.append(arpabet_to_ipa_map[base_phoneme])
                    else:
                        ipa_phonemes.append(phoneme) # Keep original if not found
                elif phoneme in arpabet_to_ipa_map:
                    ipa_phonemes.append(arpabet_to_ipa_map[phoneme])
            phoneme_list.append(ipa_phonemes)
        return phoneme_list

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
    
    def compute_word_list_frequency(self):
        """
        Compute the frequency of each word in the transcript.
        Returns a dictionary with words as keys and their frequencies as values.
        """
        word_to_freq = {}
        for word in self.word_list:
            word = word.lower()
            if word in freq_dict['Word'].values:
                freq = freq_dict[freq_dict['Word'] == word]['FREQcount'].values[0]
                word_to_freq[word] = freq
            else:
                word_to_freq[word] = 0
        return word_to_freq
    
    def compute_word_frequency_average(self):
        """
        Compute the average frequency of words in the transcript.
        Returns the average frequency as a float.
        """
        if not self.word_list_frequency:
            return 0.0
        total_freq = sum(self.word_list_frequency.values())
        average_freq = total_freq / len(self.word_list_frequency)
        return average_freq
    
    def compute_word_frequency_variance(self):
        """
        Compute the variance of word frequencies in the transcript.
        Returns the variance as a float.
        """
        if not self.word_list_frequency:
            return 0.0
        average_freq = self.compute_word_frequency_average()
        variance = sum((freq - average_freq) ** 2 for freq in self.word_list_frequency.values()) / len(self.word_list_frequency)
        return variance

if __name__ == "__main__":
    # Example usage
    video = Video(path="video_analysis/videos/linguistic_intelligence.MP4")
    print(video)

    # Print word list frequency
    print(f"Word List Frequency: {video.word_list_frequency}")
    print(f"Average Word Frequency: {video.compute_word_frequency_average()}")
    print(f"Variance of Word Frequencies: {video.compute_word_frequency_variance()}")

    # Plot a histogram with word frequencies
    frequencies = list(video.word_list_frequency.values())
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