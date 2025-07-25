import pandas as pd
# import panphon

# Load the phoneme inventory database
phoneme_database = pd.read_csv(
    "https://raw.githubusercontent.com/phoible/dev/master/data/phoible.csv",
    low_memory=False
)
# Check the columns in the phoneme database
# print(phoneme_database.columns.tolist())

# TODO need to figure out how to handle contractions - e.g. the t and s from "don't" and "someone's" are entered as distinct words
# don't should be treated as a single word, but posessives should be different
# TODO should we treat words from our videos in the same way? like split them by apostrophes?

# Load the file (tab-delimited)
freq_dict = pd.read_csv("video_analysis/SUBTLEXus74286wordstextversion.txt", sep='\t')


# Sort by frequency in subtitles
freq_dict_sorted = freq_dict.sort_values("FREQcount", ascending=False)

def extract_top_words(n):   
    """
    Extract the top n words from the DataFrame based on frequency.
    """
    return list(freq_dict_sorted.head(n)["Word"].str.lower())


class User:
    """
    A class representing a user in a video analysis system.
    This class contains the vocabulary size and a lexicon of words.
    """

    vocab_size: int

    # TODO could add a feature that calculates average vocab size from a user's CEFR level or other measures/tests

    def __init__(self, vocab_size, l1):
        self.vocab_size = vocab_size
        self.lexicon = extract_top_words(vocab_size)
        self.l1 = l1  # language name (as in phoible) of first language
        self.phonetic_inventory = self.get_phonetic_inventory()
    
    def get_phonetic_inventory(self):
        # Filter for a specific language
        phonemes = phoneme_database[phoneme_database['LanguageName'] == self.l1]['Phoneme'].unique()
        return phonemes
