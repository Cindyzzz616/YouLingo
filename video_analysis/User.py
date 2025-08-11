# TODO need to figure out how to handle contractions - e.g. the t and s from "don't" and "someone's" are entered as distinct words
# don't should be treated as a single word, but posessives should be different
# TODO should we treat words from our videos in the same way? like split them by apostrophes?

import pandas as pd
import pickle
# import panphon

##### Loading databases #####

# Loading the phoneme inventory database
phoneme_database = pd.read_csv("video_analysis/external_data/phoible.csv", low_memory=False)

# Loading the file (tab-delimited)
freq_dict = pd.read_csv("video_analysis/external_data/sublexus_corpus.txt", sep='\t')

# Sorting by frequency in subtitles
freq_dict_sorted = freq_dict.sort_values("FREQcount", ascending=False)

# Reading the word family frequency database
with open("video_analysis/external_data/word_families.pkl", "rb") as f:
    WORD_FAMILIES = pickle.load(f)

##### Helper functions #####

def extract_top_words(n):   
    """
    Extract the top n words from the DataFrame based on frequency.
    """
    return list(freq_dict_sorted.head(n)["Word"].str.lower())

def extract_top_families(n):
    """
    Extract the top n families from the word family database, and return the results as a dictionary.
    TODO figure out the upper bound of n - should be incredibly large
    """
    top_families = {}
    i = 1
    while n > 0:
        families = WORD_FAMILIES[i]
        sorted_items = sorted(
            families.items(),
            key=lambda item: item[1][0][1], # the frequency of the headword
            reverse=True
        )
        if n <= len(sorted_items):
            for item in sorted_items[:n]:
                top_families[item[0]] = item[1]
            return top_families
        else:
            for item in sorted_items:
                top_families[item[0]] = item[1]
            n -= len(sorted_items)
            i += 1
    return top_families # in case something went wrong

##### Main object class #####

class User:
    """
    A class representing a user in a video analysis system.
    This class contains the vocabulary size and a lexicon of words.
    """

    net_vocab_size: int
    word_family_size: int
    lexicon: list[str] # TODO change this to a list of Word objects?
    family_lexicon: dict[str, list[tuple]]
    l1: str
    phonetic_inventory: list[str]

    # TODO could add a feature that calculates average vocab size from a user's CEFR level or other measures/tests

    def __init__(self, net_vocab_size, l1, word_family_size=10):
        self.net_vocab_size = net_vocab_size
        self.word_family_size = word_family_size
        self.lexicon = extract_top_words(net_vocab_size) # estimating the user's exact lexicon by extracting the top frequent words
        self.family_lexicon = extract_top_families(word_family_size)
        self.l1 = l1  # language name (as in phoible) of first language
        self.phonetic_inventory = self.get_phonetic_inventory()

    def __str__(self):
        return (
            f"🔢 Vocabulary size: {self.net_vocab_size}\n"
            f"📦 Word family size: {self.word_family_size}\n"
            f"🔠 Lexicon (first 100 words): {self.lexicon[:100]}\n"
            f"🗣️ First language: {self.l1}\n"
            f"📚 Phonetic inventory of first language: {self.phonetic_inventory}\n"
        )
    
    def get_phonetic_inventory(self):
        # Filter for a specific language
        phonemes = phoneme_database[phoneme_database['LanguageName'] == self.l1]['Phoneme'].unique()
        return phonemes
    
if __name__ == '__main__':
    print(len(WORD_FAMILIES[1]))
    user = User(net_vocab_size=100, l1='French', word_family_size=1500)
    print(user)
