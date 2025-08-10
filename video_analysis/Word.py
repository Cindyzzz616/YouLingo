import re
import pandas as pd
import nltk
# from nltk.corpus import cmudict
from g2p_en import G2p
from external_data.arpa_to_ipa_map import arpabet_to_ipa_map

# from Word import Word

##### Loading dictionaries #####

# Loading CMU dictionary
CMU_DICT = nltk.corpus.cmudict.dict()

# Loading the frequency dictionary
FREQ_DICT = pd.read_csv("video_analysis/external_data/sublexus_corpus.txt", sep='\t')

# Getting headers for CLEARPOND data: Read each line, strip newline characters, ignore empty lines
with open("video_analysis/external_data/clearpondHeaders_EN.txt", "r", encoding="utf-8") as f:
    CLEARPOND_HEADERS = [line.strip() for line in f if line.strip()]

# Loading the CLEARPOND data (for phonological neighbourhood)
CLEARPOND_DATA = pd.read_csv("video_analysis/external_data/englishCPdatabase2.txt", 
                             sep='\t',
                             encoding='latin1')
CLEARPOND_DATA.columns = CLEARPOND_HEADERS

# Creating the Grapheme to Phoneme (G2P) object
g2p = G2p()

##### The word object #####

class Word:
    """
    An object representing a word in a language.
    """

    text: str
    length: int
    syllable_count: int
    tags: tuple[str]
    frequency: int
    phonemes: list[str]
    # phonological_neighbours: list[Word] # why is this illegal?

    def __init__(self, text: str):
        self.text = text
        self.length = len(text)
        self.syllable_count = self.count_syllables()
        self.tags = self.get_tags()
        self.frequency = self.calculate_frequency()
        self.phonemes = self.get_phonemes()
        self.phonological_neighbours_list = self.get_phonological_neighbours()[0]
        self.phonological_neighbours_number = self.get_phonological_neighbours()[1]
        self.phonological_neighbours_frequency = self.get_phonological_neighbours()[2]


    def __str__(self):
        return (
            f"Text: {self.text}\n"
            f"Length: {self.length}\n"
            f"Syllable count: {self.syllable_count}\n"
            f"Tags: {self.tags}\n"
            f"Frequency: {self.frequency}\n"
            f"Phonemes: {self.phonemes}\n"
            f"List of phonological neighbours: {self.phonological_neighbours_list}\n"
            f"Number of phonological neighbours: {self.phonological_neighbours_number}\n"
            f"Neighbourhood frequency: {self.phonological_neighbours_frequency}\n"
        )

    def count_syllables(self) -> int:
        """
        Count the number of syllables in a word.
        """
        word = self.text.lower()
        if word in CMU_DICT:
            # Some words have multiple pronunciations — take the first one
            return max([len([phoneme for phoneme in pron if phoneme[-1].isdigit()])
                        for pron in CMU_DICT[word]])
        else:
            # Very rough fallback for syllable counting: count vowel groups.
            return len(re.findall(r"[aeiouy]+", word.lower()))
        
    def get_tags(self):
        """
        Get the syntax tags for the word.
        """
        token = nltk.word_tokenize(self.text)
        tags = nltk.pos_tag(token)
        # tags is a tuple of strings
        return tags

    def calculate_frequency(self):
        """
        Compute the frequency of each word in the transcript.
        Returns a dictionary with words as keys and their frequencies as values.
        Returns -1 if the word is not in the corpus.
        """
        word = self.text
        if word in FREQ_DICT['Word'].values:
            freq = FREQ_DICT[FREQ_DICT['Word'] == word]['FREQcount'].values[0]
        else:
            freq = -1
        return freq
    
    def get_phonemes(self):
        """
        Get a list of phonemes of each word from the transcript. Convert each phoneme from ARPAbet to IPA.
        """
        word = self.text.lower()

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
        return ipa_phonemes
    
    def get_phonological_neighbours(self):
        word = self.text
        if word in CLEARPOND_DATA['Word'].values:
            neighbours = CLEARPOND_DATA[CLEARPOND_DATA['Word'] == word]['ePTAW'].values[0]
            neighbours = neighbours.split(';')
            number = CLEARPOND_DATA[CLEARPOND_DATA['Word'] == word]['ePTAN'].values[0]
            frequency = CLEARPOND_DATA[CLEARPOND_DATA['Word'] == word]['ePTAF'].values[0]
        else:
            neighbours = []
            number = -1
            frequency = -1
        return [neighbours, number, frequency]

##### Example usage #####
if __name__ == '__main__':
    word = Word("that")
    print(word)
