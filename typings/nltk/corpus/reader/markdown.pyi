"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.api import CategorizedCorpusReader
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

def comma_separated_string_args(func): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """
    A decorator that allows a function to be called with
    a single string of comma-separated values which become
    individual function arguments.
    """
    ...

def read_parse_blankline_block(stream, parser): # -> list[Any]:
    ...

class MarkdownBlock:
    def __init__(self, content) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    @property
    def raw(self): # -> Any:
        ...
    
    @property
    def words(self): # -> list[str]:
        ...
    
    @property
    def sents(self): # -> list[list[str]]:
        ...
    
    @property
    def paras(self): # -> list[list[list[str]]]:
        ...
    


class CodeBlock(MarkdownBlock):
    def __init__(self, language, *args) -> None:
        ...
    
    @property
    def sents(self): # -> list[list[str]]:
        ...
    
    @property
    def lines(self):
        ...
    
    @property
    def paras(self): # -> list[list[list[str]]]:
        ...
    


class MarkdownSection(MarkdownBlock):
    def __init__(self, heading, level, *args) -> None:
        ...
    


Image = ...
Link = ...
List = ...
class MarkdownCorpusReader(PlaintextCorpusReader):
    def __init__(self, *args, parser=..., **kwargs) -> None:
        ...
    


class CategorizedMarkdownCorpusReader(CategorizedCorpusReader, MarkdownCorpusReader):
    """
    A reader for markdown corpora whose documents are divided into
    categories based on their file identifiers.

    Based on nltk.corpus.reader.plaintext.CategorizedPlaintextCorpusReader:
    https://www.nltk.org/_modules/nltk/corpus/reader/api.html#CategorizedCorpusReader
    """
    def __init__(self, *args, cat_field=..., **kwargs) -> None:
        """
        Initialize the corpus reader. Categorization arguments
        (``cat_pattern``, ``cat_map``, and ``cat_file``) are passed to
        the ``CategorizedCorpusReader`` constructor.  The remaining arguments
        are passed to the ``MarkdownCorpusReader`` constructor.
        """
        ...
    
    @comma_separated_string_args
    def categories(self, fileids=...): # -> list[Any]:
        ...
    
    @comma_separated_string_args
    def fileids(self, categories=...): # -> list[str | Any] | list[Any] | Any:
        ...
    
    @comma_separated_string_args
    def raw(self, fileids=..., categories=...):
        ...
    
    @comma_separated_string_args
    def words(self, fileids=..., categories=...):
        ...
    
    @comma_separated_string_args
    def sents(self, fileids=..., categories=...):
        ...
    
    @comma_separated_string_args
    def paras(self, fileids=..., categories=...):
        ...
    
    def concatenated_view(self, reader, fileids, categories): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def metadata_reader(self, stream): # -> list[Any]:
        ...
    
    @comma_separated_string_args
    def metadata(self, fileids=..., categories=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def blockquote_reader(self, stream): # -> list[MarkdownBlock]:
        ...
    
    @comma_separated_string_args
    def blockquotes(self, fileids=..., categories=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def code_block_reader(self, stream): # -> list[CodeBlock]:
        ...
    
    @comma_separated_string_args
    def code_blocks(self, fileids=..., categories=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def image_reader(self, stream): # -> list[Image]:
        ...
    
    @comma_separated_string_args
    def images(self, fileids=..., categories=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def link_reader(self, stream): # -> list[Link]:
        ...
    
    @comma_separated_string_args
    def links(self, fileids=..., categories=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def list_reader(self, stream): # -> list[List]:
        ...
    
    @comma_separated_string_args
    def lists(self, fileids=..., categories=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def section_reader(self, stream): # -> list[MarkdownSection]:
        ...
    
    @comma_separated_string_args
    def sections(self, fileids=..., categories=...): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    


