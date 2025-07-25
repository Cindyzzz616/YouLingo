"""
This type stub file was generated by pyright.
"""

"""
This module brings together a variety of NLTK functionality for
text analysis, and provides simple, interactive interfaces.
Functionality includes: concordancing, collocation discovery,
regular expression search over tokenized strings, and
distributional similarity.
"""
ConcordanceLine = ...
class ContextIndex:
    """
    A bidirectional index between words and their 'contexts' in a text.
    The context of a word is usually defined to be the words that occur
    in a fixed window around the word; but other definitions may also
    be used by providing a custom context function.
    """
    def __init__(self, tokens, context_func=..., filter=..., key=...) -> None:
        ...
    
    def tokens(self): # -> Any:
        """
        :rtype: list(str)
        :return: The document that this context index was
            created from.
        """
        ...
    
    def word_similarity_dict(self, word): # -> dict[Any, Any]:
        """
        Return a dictionary mapping from words to 'similarity scores,'
        indicating how often these two words occur in the same
        context.
        """
        ...
    
    def similar_words(self, word, n=...):
        ...
    
    def common_contexts(self, words, fail_on_unknown=...): # -> FreqDist:
        """
        Find contexts where the specified words can all appear; and
        return a frequency distribution mapping each context to the
        number of times that context was used.

        :param words: The words used to seed the similarity search
        :type words: str
        :param fail_on_unknown: If true, then raise a value error if
            any of the given words do not occur at all in the index.
        """
        ...
    


class ConcordanceIndex:
    """
    An index that can be used to look up the offset locations at which
    a given word occurs in a document.
    """
    def __init__(self, tokens, key=...) -> None:
        """
        Construct a new concordance index.

        :param tokens: The document (list of tokens) that this
            concordance index was created from.  This list can be used
            to access the context of a given word occurrence.
        :param key: A function that maps each token to a normalized
            version that will be used as a key in the index.  E.g., if
            you use ``key=lambda s:s.lower()``, then the index will be
            case-insensitive.
        """
        ...
    
    def tokens(self): # -> Any:
        """
        :rtype: list(str)
        :return: The document that this concordance index was
            created from.
        """
        ...
    
    def offsets(self, word): # -> list[Any]:
        """
        :rtype: list(int)
        :return: A list of the offset positions at which the given
            word occurs.  If a key function was specified for the
            index, then given word's key will be looked up.
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def find_concordance(self, word, width=...): # -> list[Any]:
        """
        Find all concordance lines given the query word.

        Provided with a list of words, these will be found as a phrase.
        """
        ...
    
    def print_concordance(self, word, width=..., lines=...): # -> None:
        """
        Print concordance lines given the query word.
        :param word: The target word or phrase (a list of strings)
        :type word: str or list
        :param lines: The number of lines to display (default=25)
        :type lines: int
        :param width: The width of each line, in characters (default=80)
        :type width: int
        :param save: The option to save the concordance.
        :type save: bool
        """
        ...
    


class TokenSearcher:
    """
    A class that makes it easier to use regular expressions to search
    over tokenized strings.  The tokenized string is converted to a
    string where tokens are marked with angle brackets -- e.g.,
    ``'<the><window><is><still><open>'``.  The regular expression
    passed to the ``findall()`` method is modified to treat angle
    brackets as non-capturing parentheses, in addition to matching the
    token boundaries; and to have ``'.'`` not match the angle brackets.
    """
    def __init__(self, tokens) -> None:
        ...
    
    def findall(self, regexp): # -> list[Any]:
        """
        Find instances of the regular expression in the text.
        The text is a list of tokens, and a regexp pattern to match
        a single token must be surrounded by angle brackets.  E.g.

        >>> from nltk.text import TokenSearcher
        >>> from nltk.book import text1, text5, text9
        >>> text5.findall("<.*><.*><bro>")
        you rule bro; telling you bro; u twizted bro
        >>> text1.findall("<a>(<.*>)<man>")
        monied; nervous; dangerous; white; white; white; pious; queer; good;
        mature; white; Cape; great; wise; wise; butterless; white; fiendish;
        pale; furious; better; certain; complete; dismasted; younger; brave;
        brave; brave; brave
        >>> text9.findall("<th.*>{3,}")
        thread through those; the thought that; that the thing; the thing
        that; that that thing; through these than through; them that the;
        through the thick; them that they; thought that the

        :param regexp: A regular expression
        :type regexp: str
        """
        ...
    


class Text:
    """
    A wrapper around a sequence of simple (string) tokens, which is
    intended to support initial exploration of texts (via the
    interactive console).  Its methods perform a variety of analyses
    on the text's contexts (e.g., counting, concordancing, collocation
    discovery), and display the results.  If you wish to write a
    program which makes use of these analyses, then you should bypass
    the ``Text`` class, and use the appropriate analysis function or
    class directly instead.

    A ``Text`` is typically initialized from a given document or
    corpus.  E.g.:

    >>> import nltk.corpus
    >>> from nltk.text import Text
    >>> moby = Text(nltk.corpus.gutenberg.words('melville-moby_dick.txt'))

    """
    _COPY_TOKENS = ...
    def __init__(self, tokens, name=...) -> None:
        """
        Create a Text object.

        :param tokens: The source text.
        :type tokens: sequence of str
        """
        ...
    
    def __getitem__(self, i):
        ...
    
    def __len__(self): # -> int:
        ...
    
    def concordance(self, word, width=..., lines=...): # -> None:
        """
        Prints a concordance for ``word`` with the specified context window.
        Word matching is not case-sensitive.

        :param word: The target word or phrase (a list of strings)
        :type word: str or list
        :param width: The width of each line, in characters (default=80)
        :type width: int
        :param lines: The number of lines to display (default=25)
        :type lines: int

        :seealso: ``ConcordanceIndex``
        """
        ...
    
    def concordance_list(self, word, width=..., lines=...): # -> list[Any]:
        """
        Generate a concordance for ``word`` with the specified context window.
        Word matching is not case-sensitive.

        :param word: The target word or phrase (a list of strings)
        :type word: str or list
        :param width: The width of each line, in characters (default=80)
        :type width: int
        :param lines: The number of lines to display (default=25)
        :type lines: int

        :seealso: ``ConcordanceIndex``
        """
        ...
    
    def collocation_list(self, num=..., window_size=...): # -> list[Any]:
        """
        Return collocations derived from the text, ignoring stopwords.

            >>> from nltk.book import text4
            >>> text4.collocation_list()[:2]
            [('United', 'States'), ('fellow', 'citizens')]

        :param num: The maximum number of collocations to return.
        :type num: int
        :param window_size: The number of tokens spanned by a collocation (default=2)
        :type window_size: int
        :rtype: list(tuple(str, str))
        """
        ...
    
    def collocations(self, num=..., window_size=...): # -> None:
        """
        Print collocations derived from the text, ignoring stopwords.

            >>> from nltk.book import text4
            >>> text4.collocations() # doctest: +NORMALIZE_WHITESPACE
            United States; fellow citizens; years ago; four years; Federal
            Government; General Government; American people; Vice President; God
            bless; Chief Justice; one another; fellow Americans; Old World;
            Almighty God; Fellow citizens; Chief Magistrate; every citizen; Indian
            tribes; public debt; foreign nations


        :param num: The maximum number of collocations to print.
        :type num: int
        :param window_size: The number of tokens spanned by a collocation (default=2)
        :type window_size: int
        """
        ...
    
    def count(self, word): # -> int:
        """
        Count the number of times this word appears in the text.
        """
        ...
    
    def index(self, word): # -> int:
        """
        Find the index of the first occurrence of the word in the text.
        """
        ...
    
    def readability(self, method):
        ...
    
    def similar(self, word, num=...): # -> None:
        """
        Distributional similarity: find other words which appear in the
        same contexts as the specified word; list most similar words first.

        :param word: The word used to seed the similarity search
        :type word: str
        :param num: The number of words to generate (default=20)
        :type num: int
        :seealso: ContextIndex.similar_words()
        """
        ...
    
    def common_contexts(self, words, num=...): # -> None:
        """
        Find contexts where the specified words appear; list
        most frequent common contexts first.

        :param words: The words used to seed the similarity search
        :type words: str
        :param num: The number of words to generate (default=20)
        :type num: int
        :seealso: ContextIndex.common_contexts()
        """
        ...
    
    def dispersion_plot(self, words): # -> None:
        """
        Produce a plot showing the distribution of the words through the text.
        Requires pylab to be installed.

        :param words: The words to be plotted
        :type words: list(str)
        :seealso: nltk.draw.dispersion_plot()
        """
        ...
    
    def generate(self, length=..., text_seed=..., random_seed=...): # -> str:
        """
        Print random text, generated using a trigram language model.
        See also `help(nltk.lm)`.

        :param length: The length of text to generate (default=100)
        :type length: int

        :param text_seed: Generation can be conditioned on preceding context.
        :type text_seed: list(str)

        :param random_seed: A random seed or an instance of `random.Random`. If provided,
            makes the random sampling part of generation reproducible. (default=42)
        :type random_seed: int
        """
        ...
    
    def plot(self, *args):
        """
        See documentation for FreqDist.plot()
        :seealso: nltk.prob.FreqDist.plot()
        """
        ...
    
    def vocab(self): # -> FreqDist:
        """
        :seealso: nltk.prob.FreqDist
        """
        ...
    
    def findall(self, regexp): # -> None:
        """
        Find instances of the regular expression in the text.
        The text is a list of tokens, and a regexp pattern to match
        a single token must be surrounded by angle brackets.  E.g.

        >>> from nltk.book import text1, text5, text9
        >>> text5.findall("<.*><.*><bro>")
        you rule bro; telling you bro; u twizted bro
        >>> text1.findall("<a>(<.*>)<man>")
        monied; nervous; dangerous; white; white; white; pious; queer; good;
        mature; white; Cape; great; wise; wise; butterless; white; fiendish;
        pale; furious; better; certain; complete; dismasted; younger; brave;
        brave; brave; brave
        >>> text9.findall("<th.*>{3,}")
        thread through those; the thought that; that the thing; the thing
        that; that that thing; through these than through; them that the;
        through the thick; them that they; thought that the

        :param regexp: A regular expression
        :type regexp: str
        """
        ...
    
    _CONTEXT_RE = ...
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class TextCollection(Text):
    """A collection of texts, which can be loaded with list of texts, or
    with a corpus consisting of one or more texts, and which supports
    counting, concordancing, collocation discovery, etc.  Initialize a
    TextCollection as follows:

    >>> import nltk.corpus
    >>> from nltk.text import TextCollection
    >>> from nltk.book import text1, text2, text3
    >>> gutenberg = TextCollection(nltk.corpus.gutenberg)
    >>> mytexts = TextCollection([text1, text2, text3])

    Iterating over a TextCollection produces all the tokens of all the
    texts in order.
    """
    def __init__(self, source) -> None:
        ...
    
    def tf(self, term, text):
        """The frequency of the term in text."""
        ...
    
    def idf(self, term): # -> float:
        """The number of texts in the corpus divided by the
        number of texts that the term appears in.
        If a term does not appear in the corpus, 0.0 is returned."""
        ...
    
    def tf_idf(self, term, text):
        ...
    


def demo(): # -> None:
    ...

if __name__ == "__main__":
    ...
__all__ = ["ContextIndex", "ConcordanceIndex", "TokenSearcher", "Text", "TextCollection"]
