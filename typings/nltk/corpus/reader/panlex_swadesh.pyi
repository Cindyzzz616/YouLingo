"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.wordlist import WordListCorpusReader

PanlexLanguage = ...
class PanlexSwadeshCorpusReader(WordListCorpusReader):
    """
    This is a class to read the PanLex Swadesh list from

    David Kamholz, Jonathan Pool, and Susan M. Colowick (2014).
    PanLex: Building a Resource for Panlingual Lexical Translation.
    In LREC. http://www.lrec-conf.org/proceedings/lrec2014/pdf/1029_Paper.pdf

    License: CC0 1.0 Universal
    https://creativecommons.org/publicdomain/zero/1.0/legalcode
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def license(self): # -> Literal['CC0 1.0 Universal']:
        ...
    
    def language_codes(self): # -> dict_keys[Any, PanlexLanguage]:
        ...
    
    def get_languages(self): # -> Generator[PanlexLanguage, Any, None]:
        ...
    
    def get_macrolanguages(self): # -> defaultdict[Any, list[Any]]:
        ...
    
    def words_by_lang(self, lang_code): # -> list[list[str]]:
        """
        :return: a list of list(str)
        """
        ...
    
    def words_by_iso639(self, iso63_code): # -> list[list[str]]:
        """
        :return: a list of list(str)
        """
        ...
    
    def entries(self, fileids=...): # -> list[tuple[Any, ...]]:
        """
        :return: a tuple of words for the specified fileids.
        """
        ...
    


