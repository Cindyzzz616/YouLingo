"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.xmldocs import XMLCorpusReader, XMLCorpusView

"""Corpus reader for the XML version of the British National Corpus."""
class BNCCorpusReader(XMLCorpusReader):
    r"""Corpus reader for the XML version of the British National Corpus.

    For access to the complete XML data structure, use the ``xml()``
    method.  For access to simple word lists and tagged word lists, use
    ``words()``, ``sents()``, ``tagged_words()``, and ``tagged_sents()``.

    You can obtain the full version of the BNC corpus at
    https://www.ota.ox.ac.uk/desc/2554

    If you extracted the archive to a directory called `BNC`, then you can
    instantiate the reader as::

        BNCCorpusReader(root='BNC/Texts/', fileids=r'[A-K]/\w*/\w*\.xml')

    """
    def __init__(self, root, fileids, lazy=...) -> None:
        ...
    
    def words(self, fileids=..., strip_space=..., stem=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        """
        :return: the given file(s) as a list of words
            and punctuation symbols.
        :rtype: list(str)

        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    
    def tagged_words(self, fileids=..., c5=..., strip_space=..., stem=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        """
        :return: the given file(s) as a list of tagged
            words and punctuation symbols, encoded as tuples
            ``(word,tag)``.
        :rtype: list(tuple(str,str))

        :param c5: If true, then the tags used will be the more detailed
            c5 tags.  Otherwise, the simplified tags will be used.
        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    
    def sents(self, fileids=..., strip_space=..., stem=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        """
        :return: the given file(s) as a list of
            sentences or utterances, each encoded as a list of word
            strings.
        :rtype: list(list(str))

        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    
    def tagged_sents(self, fileids=..., c5=..., strip_space=..., stem=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        """
        :return: the given file(s) as a list of
            sentences, each encoded as a list of ``(word,tag)`` tuples.
        :rtype: list(list(tuple(str,str)))

        :param c5: If true, then the tags used will be the more detailed
            c5 tags.  Otherwise, the simplified tags will be used.
        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    


class BNCSentence(list):
    """
    A list of words, augmented by an attribute ``num`` used to record
    the sentence identifier (the ``n`` attribute from the XML).
    """
    def __init__(self, num, items) -> None:
        ...
    


class BNCWordView(XMLCorpusView):
    """
    A stream backed corpus view specialized for use with the BNC corpus.
    """
    tags_to_ignore = ...
    def __init__(self, fileid, sent, tag, strip_space, stem) -> None:
        """
        :param fileid: The name of the underlying file.
        :param sent: If true, include sentence bracketing.
        :param tag: The name of the tagset to use, or None for no tags.
        :param strip_space: If true, strip spaces from word tokens.
        :param stem: If true, then substitute stems for words.
        """
        ...
    
    def handle_header(self, elt, context): # -> None:
        ...
    
    def handle_elt(self, elt, context): # -> BNCSentence | tuple[Any | LiteralString | Literal[''], Any] | LiteralString | Literal['']:
        ...
    
    def handle_word(self, elt): # -> tuple[Any | LiteralString | Literal[''], Any] | LiteralString | Literal['']:
        ...
    
    def handle_sent(self, elt): # -> BNCSentence:
        ...
    


