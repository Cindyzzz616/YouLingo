# TODO need to figure out how to handle contractions - e.g. the t and s from "don't" and "someone's" are entered as distinct words
# don't should be treated as a single word, but posessives should be different
# TODO should we treat words from our videos in the same way? like split them by apostrophes?

import pandas as pd
# import panphon

##### Loading databases #####

# Load the phoneme inventory database
phoneme_database = pd.read_csv("video_analysis/external_data/phoible.csv", low_memory=False)

# Load the file (tab-delimited)
freq_dict = pd.read_csv("video_analysis/external_data/sublexus_corpus.txt", sep='\t')

# Sort by frequency in subtitles
freq_dict_sorted = freq_dict.sort_values("FREQcount", ascending=False)

##### Helper functions #####

def extract_top_words(n):   
    """
    Extract the top n words from the DataFrame based on frequency.
    """
    return list(freq_dict_sorted.head(n)["Word"].str.lower())

##### Main object class #####

class User:
    """
    A class representing a user in a video analysis system.
    This class contains the vocabulary size and a lexicon of words.
    """

    l1: str
    net_vocab_size: int

    # TODO could add a feature that calculates average vocab size from a user's CEFR level or other measures/tests

    def __init__(self, net_vocab_size, l1, word_family_size=1000):
        self.net_vocab_size = net_vocab_size
        self.word_family_size = word_family_size
        self.lexicon = extract_top_words(net_vocab_size)
        self.l1 = l1  # language name (as in phoible) of first language
        self.phonetic_inventory = self.get_phonetic_inventory()

    def __str__(self):
        return (
            f"🔢 Vocabulary size: {self.net_vocab_size}\n"
            f"🔠 Lexicon (first 100 words): {self.lexicon[:100]}\n"
            f"🗣️ First language: {self.l1}\n"
            f"📚 Phonetic inventory of first language: {self.phonetic_inventory}\n"
        )
    
    def get_phonetic_inventory(self):
        # Filter for a specific language
        phonemes = phoneme_database[phoneme_database['LanguageName'] == self.l1]['Phoneme'].unique()
        return phonemes
    
if __name__ == '__main__':
    user = User(1000, 'French')
    print(user)
