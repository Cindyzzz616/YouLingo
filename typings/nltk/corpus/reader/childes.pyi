"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.xmldocs import XMLCorpusReader

"""
Corpus reader for the XML version of the CHILDES corpus.
"""
__docformat__ = ...
NS = ...
class CHILDESCorpusReader(XMLCorpusReader):
    """
    Corpus reader for the XML version of the CHILDES corpus.
    The CHILDES corpus is available at ``https://childes.talkbank.org/``. The XML
    version of CHILDES is located at ``https://childes.talkbank.org/data-xml/``.
    Copy the needed parts of the CHILDES XML corpus into the NLTK data directory
    (``nltk_data/corpora/CHILDES/``).

    For access to the file text use the usual nltk functions,
    ``words()``, ``sents()``, ``tagged_words()`` and ``tagged_sents()``.
    """
    def __init__(self, root, fileids, lazy=...) -> None:
        ...
    
    def words(self, fileids=..., speaker=..., stem=..., relation=..., strip_space=..., replace=...): # -> list[Any] | LazyConcatenation:
        """
        :return: the given file(s) as a list of words
        :rtype: list(str)

        :param speaker: If specified, select specific speaker(s) defined
            in the corpus. Default is 'ALL' (all participants). Common choices
            are 'CHI' (the child), 'MOT' (mother), ['CHI','MOT'] (exclude
            researchers)
        :param stem: If true, then use word stems instead of word strings.
        :param relation: If true, then return tuples of (stem, index,
            dependent_index)
        :param strip_space: If true, then strip trailing spaces from word
            tokens. Otherwise, leave the spaces on the tokens.
        :param replace: If true, then use the replaced (intended) word instead
            of the original word (e.g., 'wat' will be replaced with 'watch')
        """
        ...
    
    def tagged_words(self, fileids=..., speaker=..., stem=..., relation=..., strip_space=..., replace=...): # -> list[Any] | LazyConcatenation:
        """
        :return: the given file(s) as a list of tagged
            words and punctuation symbols, encoded as tuples
            ``(word,tag)``.
        :rtype: list(tuple(str,str))

        :param speaker: If specified, select specific speaker(s) defined
            in the corpus. Default is 'ALL' (all participants). Common choices
            are 'CHI' (the child), 'MOT' (mother), ['CHI','MOT'] (exclude
            researchers)
        :param stem: If true, then use word stems instead of word strings.
        :param relation: If true, then return tuples of (stem, index,
            dependent_index)
        :param strip_space: If true, then strip trailing spaces from word
            tokens. Otherwise, leave the spaces on the tokens.
        :param replace: If true, then use the replaced (intended) word instead
            of the original word (e.g., 'wat' will be replaced with 'watch')
        """
        ...
    
    def sents(self, fileids=..., speaker=..., stem=..., relation=..., strip_space=..., replace=...): # -> list[Any] | LazyConcatenation:
        """
        :return: the given file(s) as a list of sentences or utterances, each
            encoded as a list of word strings.
        :rtype: list(list(str))

        :param speaker: If specified, select specific speaker(s) defined
            in the corpus. Default is 'ALL' (all participants). Common choices
            are 'CHI' (the child), 'MOT' (mother), ['CHI','MOT'] (exclude
            researchers)
        :param stem: If true, then use word stems instead of word strings.
        :param relation: If true, then return tuples of ``(str,pos,relation_list)``.
            If there is manually-annotated relation info, it will return
            tuples of ``(str,pos,test_relation_list,str,pos,gold_relation_list)``
        :param strip_space: If true, then strip trailing spaces from word
            tokens. Otherwise, leave the spaces on the tokens.
        :param replace: If true, then use the replaced (intended) word instead
            of the original word (e.g., 'wat' will be replaced with 'watch')
        """
        ...
    
    def tagged_sents(self, fileids=..., speaker=..., stem=..., relation=..., strip_space=..., replace=...): # -> list[Any] | LazyConcatenation:
        """
        :return: the given file(s) as a list of
            sentences, each encoded as a list of ``(word,tag)`` tuples.
        :rtype: list(list(tuple(str,str)))

        :param speaker: If specified, select specific speaker(s) defined
            in the corpus. Default is 'ALL' (all participants). Common choices
            are 'CHI' (the child), 'MOT' (mother), ['CHI','MOT'] (exclude
            researchers)
        :param stem: If true, then use word stems instead of word strings.
        :param relation: If true, then return tuples of ``(str,pos,relation_list)``.
            If there is manually-annotated relation info, it will return
            tuples of ``(str,pos,test_relation_list,str,pos,gold_relation_list)``
        :param strip_space: If true, then strip trailing spaces from word
            tokens. Otherwise, leave the spaces on the tokens.
        :param replace: If true, then use the replaced (intended) word instead
            of the original word (e.g., 'wat' will be replaced with 'watch')
        """
        ...
    
    def corpus(self, fileids=...): # -> list[dict[Any, Any]] | LazyMap:
        """
        :return: the given file(s) as a dict of ``(corpus_property_key, value)``
        :rtype: list(dict)
        """
        ...
    
    def participants(self, fileids=...): # -> list[defaultdict[Any, Any]] | LazyMap:
        """
        :return: the given file(s) as a dict of
            ``(participant_property_key, value)``
        :rtype: list(dict)
        """
        ...
    
    def age(self, fileids=..., speaker=..., month=...): # -> list[int | str | None] | LazyMap:
        """
        :return: the given file(s) as string or int
        :rtype: list or int

        :param month: If true, return months instead of year-month-date
        """
        ...
    
    def convert_age(self, age_year): # -> int:
        "Caclculate age in months from a string in CHILDES format"
        ...
    
    def MLU(self, fileids=..., speaker=...): # -> list[float | int] | LazyMap:
        """
        :return: the given file(s) as a floating number
        :rtype: list(float)
        """
        ...
    
    childes_url_base = ...
    def webview_file(self, fileid, urlbase=...): # -> None:
        """Map a corpus file to its web version on the CHILDES website,
        and open it in a web browser.

        The complete URL to be used is:
            childes.childes_url_base + urlbase + fileid.replace('.xml', '.cha')

        If no urlbase is passed, we try to calculate it.  This
        requires that the childes corpus was set up to mirror the
        folder hierarchy under childes.psy.cmu.edu/data-xml/, e.g.:
        nltk_data/corpora/childes/Eng-USA/Cornell/??? or
        nltk_data/corpora/childes/Romance/Spanish/Aguirre/???

        The function first looks (as a special case) if "Eng-USA" is
        on the path consisting of <corpus root>+fileid; then if
        "childes", possibly followed by "data-xml", appears. If neither
        one is found, we use the unmodified fileid and hope for the best.
        If this is not right, specify urlbase explicitly, e.g., if the
        corpus root points to the Cornell folder, urlbase='Eng-USA/Cornell'.
        """
        ...
    


def demo(corpus_root=...): # -> None:
    """
    The CHILDES corpus should be manually downloaded and saved
    to ``[NLTK_Data_Dir]/corpora/childes/``
    """
    ...

if __name__ == "__main__":
    ...
