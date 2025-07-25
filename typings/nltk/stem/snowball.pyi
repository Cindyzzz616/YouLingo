"""
This type stub file was generated by pyright.
"""

from nltk.stem import porter
from nltk.stem.api import StemmerI

"""
Snowball stemmers

This module provides a port of the Snowball stemmers
developed by Martin Porter.

There is also a demo function: `snowball.demo()`.

"""
class SnowballStemmer(StemmerI):
    """
    Snowball Stemmer

    The following languages are supported:
    Arabic, Danish, Dutch, English, Finnish, French, German,
    Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian,
    Spanish and Swedish.

    The algorithm for English is documented here:

        Porter, M. \"An algorithm for suffix stripping.\"
        Program 14.3 (1980): 130-137.

    The algorithms have been developed by Martin Porter.
    These stemmers are called Snowball, because Porter created
    a programming language with this name for creating
    new stemming algorithms. There is more information available
    at http://snowball.tartarus.org/

    The stemmer is invoked as shown below:

    >>> from nltk.stem import SnowballStemmer # See which languages are supported
    >>> print(" ".join(SnowballStemmer.languages)) # doctest: +NORMALIZE_WHITESPACE
    arabic danish dutch english finnish french german hungarian
    italian norwegian porter portuguese romanian russian
    spanish swedish
    >>> stemmer = SnowballStemmer("german") # Choose a language
    >>> stemmer.stem("Autobahnen") # Stem a word
    'autobahn'

    Invoking the stemmers that way is useful if you do not know the
    language to be stemmed at runtime. Alternatively, if you already know
    the language, then you can invoke the language specific stemmer directly:

    >>> from nltk.stem.snowball import GermanStemmer
    >>> stemmer = GermanStemmer()
    >>> stemmer.stem("Autobahnen")
    'autobahn'

    :param language: The language whose subclass is instantiated.
    :type language: str or unicode
    :param ignore_stopwords: If set to True, stopwords are
                             not stemmed and returned unchanged.
                             Set to False by default.
    :type ignore_stopwords: bool
    :raise ValueError: If there is no stemmer for the specified
                           language, a ValueError is raised.
    """
    languages = ...
    def __init__(self, language, ignore_stopwords=...) -> None:
        ...
    
    def stem(self, token): # -> Any:
        ...
    


class _LanguageSpecificStemmer(StemmerI):
    """
    This helper subclass offers the possibility
    to invoke a specific stemmer directly.
    This is useful if you already know the language to be stemmed at runtime.

    Create an instance of the Snowball stemmer.

    :param ignore_stopwords: If set to True, stopwords are
                             not stemmed and returned unchanged.
                             Set to False by default.
    :type ignore_stopwords: bool
    """
    def __init__(self, ignore_stopwords=...) -> None:
        ...
    
    def __repr__(self): # -> str:
        """
        Print out the string representation of the respective class.

        """
        ...
    


class PorterStemmer(_LanguageSpecificStemmer, porter.PorterStemmer):
    """
    A word stemmer based on the original Porter stemming algorithm.

        Porter, M. \"An algorithm for suffix stripping.\"
        Program 14.3 (1980): 130-137.

    A few minor modifications have been made to Porter's basic
    algorithm.  See the source code of the module
    nltk.stem.porter for more information.

    """
    def __init__(self, ignore_stopwords=...) -> None:
        ...
    


class _ScandinavianStemmer(_LanguageSpecificStemmer):
    """
    This subclass encapsulates a method for defining the string region R1.
    It is used by the Danish, Norwegian, and Swedish stemmer.

    """
    ...


class _StandardStemmer(_LanguageSpecificStemmer):
    """
    This subclass encapsulates two methods for defining the standard versions
    of the string regions R1, R2, and RV.

    """
    ...


class ArabicStemmer(_StandardStemmer):
    """
    https://github.com/snowballstem/snowball/blob/master/algorithms/arabic/stem_Unicode.sbl (Original Algorithm)
    The Snowball Arabic light Stemmer
    Algorithm:

    - Assem Chelli
    - Abdelkrim Aries
    - Lakhdar Benzahia

    NLTK Version Author:

    - Lakhdar Benzahia
    """
    __vocalization = ...
    __kasheeda = ...
    __arabic_punctuation_marks = ...
    __last_hamzat = ...
    __initial_hamzat = ...
    __waw_hamza = ...
    __yeh_hamza = ...
    __alefat = ...
    __checks1 = ...
    __checks2 = ...
    __suffix_noun_step1a = ...
    __suffix_noun_step1b = ...
    __suffix_noun_step2a = ...
    __suffix_noun_step2b = ...
    __suffix_noun_step2c1 = ...
    __suffix_noun_step2c2 = ...
    __suffix_noun_step3 = ...
    __suffix_verb_step1 = ...
    __suffix_verb_step2a = ...
    __suffix_verb_step2b = ...
    __suffix_verb_step2c = ...
    __suffix_all_alef_maqsura = ...
    __prefix_step1 = ...
    __prefix_step2a = ...
    __prefix_step2b = ...
    __prefix_step3a_noun = ...
    __prefix_step3b_noun = ...
    __prefix_step3_verb = ...
    __prefix_step4_verb = ...
    __conjugation_suffix_verb_1 = ...
    __conjugation_suffix_verb_2 = ...
    __conjugation_suffix_verb_3 = ...
    __conjugation_suffix_verb_4 = ...
    __conjugation_suffix_verb_past = ...
    __conjugation_suffix_verb_present = ...
    __conjugation_suffix_noun_1 = ...
    __conjugation_suffix_noun_2 = ...
    __conjugation_suffix_noun_3 = ...
    __prefixes1 = ...
    __articles_3len = ...
    __articles_2len = ...
    __prepositions1 = ...
    __prepositions2 = ...
    is_verb = ...
    is_noun = ...
    is_defined = ...
    suffixes_verb_step1_success = ...
    suffix_verb_step2a_success = ...
    suffix_verb_step2b_success = ...
    suffix_noun_step2c2_success = ...
    suffix_noun_step1a_success = ...
    suffix_noun_step2a_success = ...
    suffix_noun_step2b_success = ...
    suffixe_noun_step1b_success = ...
    prefix_step2a_success = ...
    prefix_step3a_noun_success = ...
    prefix_step3b_noun_success = ...
    def stem(self, word): # -> str:
        """
        Stem an Arabic word and return the stemmed form.

        :param word: string
        :return: string
        """
        ...
    


class DanishStemmer(_ScandinavianStemmer):
    """
    The Danish Snowball stemmer.

    :cvar __vowels: The Danish vowels.
    :type __vowels: unicode
    :cvar __consonants: The Danish consonants.
    :type __consonants: unicode
    :cvar __double_consonants: The Danish double consonants.
    :type __double_consonants: tuple
    :cvar __s_ending: Letters that may directly appear before a word final 's'.
    :type __s_ending: unicode
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :note: A detailed description of the Danish
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/danish/stemmer.html

    """
    __vowels = ...
    __consonants = ...
    __double_consonants = ...
    __s_ending = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    def stem(self, word):
        """
        Stem a Danish word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class DutchStemmer(_StandardStemmer):
    """
    The Dutch Snowball stemmer.

    :cvar __vowels: The Dutch vowels.
    :type __vowels: unicode
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step3b_suffixes: Suffixes to be deleted in step 3b of the algorithm.
    :type __step3b_suffixes: tuple
    :note: A detailed description of the Dutch
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/dutch/stemmer.html

    """
    __vowels = ...
    __step1_suffixes = ...
    __step3b_suffixes = ...
    def stem(self, word):
        """
        Stem a Dutch word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class EnglishStemmer(_StandardStemmer):
    """
    The English Snowball stemmer.

    :cvar __vowels: The English vowels.
    :type __vowels: unicode
    :cvar __double_consonants: The English double consonants.
    :type __double_consonants: tuple
    :cvar __li_ending: Letters that may directly appear before a word final 'li'.
    :type __li_ending: unicode
    :cvar __step0_suffixes: Suffixes to be deleted in step 0 of the algorithm.
    :type __step0_suffixes: tuple
    :cvar __step1a_suffixes: Suffixes to be deleted in step 1a of the algorithm.
    :type __step1a_suffixes: tuple
    :cvar __step1b_suffixes: Suffixes to be deleted in step 1b of the algorithm.
    :type __step1b_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :cvar __step4_suffixes: Suffixes to be deleted in step 4 of the algorithm.
    :type __step4_suffixes: tuple
    :cvar __step5_suffixes: Suffixes to be deleted in step 5 of the algorithm.
    :type __step5_suffixes: tuple
    :cvar __special_words: A dictionary containing words
                           which have to be stemmed specially.
    :type __special_words: dict
    :note: A detailed description of the English
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/english/stemmer.html
    """
    __vowels = ...
    __double_consonants = ...
    __li_ending = ...
    __step0_suffixes = ...
    __step1a_suffixes = ...
    __step1b_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    __step4_suffixes = ...
    __step5_suffixes = ...
    __special_words = ...
    def stem(self, word):
        """
        Stem an English word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class FinnishStemmer(_StandardStemmer):
    """
    The Finnish Snowball stemmer.

    :cvar __vowels: The Finnish vowels.
    :type __vowels: unicode
    :cvar __restricted_vowels: A subset of the Finnish vowels.
    :type __restricted_vowels: unicode
    :cvar __long_vowels: The Finnish vowels in their long forms.
    :type __long_vowels: tuple
    :cvar __consonants: The Finnish consonants.
    :type __consonants: unicode
    :cvar __double_consonants: The Finnish double consonants.
    :type __double_consonants: tuple
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :cvar __step4_suffixes: Suffixes to be deleted in step 4 of the algorithm.
    :type __step4_suffixes: tuple
    :note: A detailed description of the Finnish
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/finnish/stemmer.html
    """
    __vowels = ...
    __restricted_vowels = ...
    __long_vowels = ...
    __consonants = ...
    __double_consonants = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    __step4_suffixes = ...
    def stem(self, word):
        """
        Stem a Finnish word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class FrenchStemmer(_StandardStemmer):
    """
    The French Snowball stemmer.

    :cvar __vowels: The French vowels.
    :type __vowels: unicode
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2a_suffixes: Suffixes to be deleted in step 2a of the algorithm.
    :type __step2a_suffixes: tuple
    :cvar __step2b_suffixes: Suffixes to be deleted in step 2b of the algorithm.
    :type __step2b_suffixes: tuple
    :cvar __step4_suffixes: Suffixes to be deleted in step 4 of the algorithm.
    :type __step4_suffixes: tuple
    :note: A detailed description of the French
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/french/stemmer.html
    """
    __vowels = ...
    __step1_suffixes = ...
    __step2a_suffixes = ...
    __step2b_suffixes = ...
    __step4_suffixes = ...
    def stem(self, word):
        """
        Stem a French word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class GermanStemmer(_StandardStemmer):
    """
    The German Snowball stemmer.

    :cvar __vowels: The German vowels.
    :type __vowels: unicode
    :cvar __s_ending: Letters that may directly appear before a word final 's'.
    :type __s_ending: unicode
    :cvar __st_ending: Letter that may directly appear before a word final 'st'.
    :type __st_ending: unicode
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :note: A detailed description of the German
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/german/stemmer.html

    """
    __vowels = ...
    __s_ending = ...
    __st_ending = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    def stem(self, word):
        """
        Stem a German word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class HungarianStemmer(_LanguageSpecificStemmer):
    """
    The Hungarian Snowball stemmer.

    :cvar __vowels: The Hungarian vowels.
    :type __vowels: unicode
    :cvar __digraphs: The Hungarian digraphs.
    :type __digraphs: tuple
    :cvar __double_consonants: The Hungarian double consonants.
    :type __double_consonants: tuple
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :cvar __step4_suffixes: Suffixes to be deleted in step 4 of the algorithm.
    :type __step4_suffixes: tuple
    :cvar __step5_suffixes: Suffixes to be deleted in step 5 of the algorithm.
    :type __step5_suffixes: tuple
    :cvar __step6_suffixes: Suffixes to be deleted in step 6 of the algorithm.
    :type __step6_suffixes: tuple
    :cvar __step7_suffixes: Suffixes to be deleted in step 7 of the algorithm.
    :type __step7_suffixes: tuple
    :cvar __step8_suffixes: Suffixes to be deleted in step 8 of the algorithm.
    :type __step8_suffixes: tuple
    :cvar __step9_suffixes: Suffixes to be deleted in step 9 of the algorithm.
    :type __step9_suffixes: tuple
    :note: A detailed description of the Hungarian
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/hungarian/stemmer.html

    """
    __vowels = ...
    __digraphs = ...
    __double_consonants = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    __step4_suffixes = ...
    __step5_suffixes = ...
    __step6_suffixes = ...
    __step7_suffixes = ...
    __step8_suffixes = ...
    __step9_suffixes = ...
    def stem(self, word):
        """
        Stem an Hungarian word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class ItalianStemmer(_StandardStemmer):
    """
    The Italian Snowball stemmer.

    :cvar __vowels: The Italian vowels.
    :type __vowels: unicode
    :cvar __step0_suffixes: Suffixes to be deleted in step 0 of the algorithm.
    :type __step0_suffixes: tuple
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :note: A detailed description of the Italian
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/italian/stemmer.html

    """
    __vowels = ...
    __step0_suffixes = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    def stem(self, word):
        """
        Stem an Italian word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class NorwegianStemmer(_ScandinavianStemmer):
    """
    The Norwegian Snowball stemmer.

    :cvar __vowels: The Norwegian vowels.
    :type __vowels: unicode
    :cvar __s_ending: Letters that may directly appear before a word final 's'.
    :type __s_ending: unicode
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :note: A detailed description of the Norwegian
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/norwegian/stemmer.html

    """
    __vowels = ...
    __s_ending = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    def stem(self, word):
        """
        Stem a Norwegian word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class PortugueseStemmer(_StandardStemmer):
    """
    The Portuguese Snowball stemmer.

    :cvar __vowels: The Portuguese vowels.
    :type __vowels: unicode
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step4_suffixes: Suffixes to be deleted in step 4 of the algorithm.
    :type __step4_suffixes: tuple
    :note: A detailed description of the Portuguese
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/portuguese/stemmer.html

    """
    __vowels = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step4_suffixes = ...
    def stem(self, word):
        """
        Stem a Portuguese word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class RomanianStemmer(_StandardStemmer):
    """
    The Romanian Snowball stemmer.

    :cvar __vowels: The Romanian vowels.
    :type __vowels: unicode
    :cvar __step0_suffixes: Suffixes to be deleted in step 0 of the algorithm.
    :type __step0_suffixes: tuple
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :note: A detailed description of the Romanian
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/romanian/stemmer.html

    """
    __vowels = ...
    __step0_suffixes = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    def stem(self, word):
        """
        Stem a Romanian word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class RussianStemmer(_LanguageSpecificStemmer):
    """
    The Russian Snowball stemmer.

    :cvar __perfective_gerund_suffixes: Suffixes to be deleted.
    :type __perfective_gerund_suffixes: tuple
    :cvar __adjectival_suffixes: Suffixes to be deleted.
    :type __adjectival_suffixes: tuple
    :cvar __reflexive_suffixes: Suffixes to be deleted.
    :type __reflexive_suffixes: tuple
    :cvar __verb_suffixes: Suffixes to be deleted.
    :type __verb_suffixes: tuple
    :cvar __noun_suffixes: Suffixes to be deleted.
    :type __noun_suffixes: tuple
    :cvar __superlative_suffixes: Suffixes to be deleted.
    :type __superlative_suffixes: tuple
    :cvar __derivational_suffixes: Suffixes to be deleted.
    :type __derivational_suffixes: tuple
    :note: A detailed description of the Russian
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/russian/stemmer.html

    """
    __perfective_gerund_suffixes = ...
    __adjectival_suffixes = ...
    __reflexive_suffixes = ...
    __verb_suffixes = ...
    __noun_suffixes = ...
    __superlative_suffixes = ...
    __derivational_suffixes = ...
    def stem(self, word):
        """
        Stem a Russian word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class SpanishStemmer(_StandardStemmer):
    """
    The Spanish Snowball stemmer.

    :cvar __vowels: The Spanish vowels.
    :type __vowels: unicode
    :cvar __step0_suffixes: Suffixes to be deleted in step 0 of the algorithm.
    :type __step0_suffixes: tuple
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2a_suffixes: Suffixes to be deleted in step 2a of the algorithm.
    :type __step2a_suffixes: tuple
    :cvar __step2b_suffixes: Suffixes to be deleted in step 2b of the algorithm.
    :type __step2b_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :note: A detailed description of the Spanish
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/spanish/stemmer.html

    """
    __vowels = ...
    __step0_suffixes = ...
    __step1_suffixes = ...
    __step2a_suffixes = ...
    __step2b_suffixes = ...
    __step3_suffixes = ...
    def stem(self, word):
        """
        Stem a Spanish word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


class SwedishStemmer(_ScandinavianStemmer):
    """
    The Swedish Snowball stemmer.

    :cvar __vowels: The Swedish vowels.
    :type __vowels: unicode
    :cvar __s_ending: Letters that may directly appear before a word final 's'.
    :type __s_ending: unicode
    :cvar __step1_suffixes: Suffixes to be deleted in step 1 of the algorithm.
    :type __step1_suffixes: tuple
    :cvar __step2_suffixes: Suffixes to be deleted in step 2 of the algorithm.
    :type __step2_suffixes: tuple
    :cvar __step3_suffixes: Suffixes to be deleted in step 3 of the algorithm.
    :type __step3_suffixes: tuple
    :note: A detailed description of the Swedish
           stemming algorithm can be found under
           http://snowball.tartarus.org/algorithms/swedish/stemmer.html

    """
    __vowels = ...
    __s_ending = ...
    __step1_suffixes = ...
    __step2_suffixes = ...
    __step3_suffixes = ...
    def stem(self, word):
        """
        Stem a Swedish word and return the stemmed form.

        :param word: The word that is stemmed.
        :type word: str or unicode
        :return: The stemmed form.
        :rtype: unicode

        """
        ...
    


def demo(): # -> None:
    """
    This function provides a demonstration of the Snowball stemmers.

    After invoking this function and specifying a language,
    it stems an excerpt of the Universal Declaration of Human Rights
    (which is a part of the NLTK corpus collection) and then prints
    out the original and the stemmed text.

    """
    ...

