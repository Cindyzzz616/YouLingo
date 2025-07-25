"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *

"""
Read lines from the Prepositional Phrase Attachment Corpus.

The PP Attachment Corpus contains several files having the format:

sentence_id verb noun1 preposition noun2 attachment

For example:

42960 gives authority to administration V
46742 gives inventors of microchip N

The PP attachment is to the verb phrase (V) or noun phrase (N), i.e.:

(VP gives (NP authority) (PP to administration))
(VP gives (NP inventors (PP of microchip)))

The corpus contains the following files:

training:   training set
devset:     development test set, used for algorithm development.
test:       test set, used to report results
bitstrings: word classes derived from Mutual Information Clustering for the Wall Street Journal.

Ratnaparkhi, Adwait (1994). A Maximum Entropy Model for Prepositional
Phrase Attachment.  Proceedings of the ARPA Human Language Technology
Conference.  [http://www.cis.upenn.edu/~adwait/papers/hlt94.ps]

The PP Attachment Corpus is distributed with NLTK with the permission
of the author.
"""
class PPAttachment:
    def __init__(self, sent, verb, noun1, prep, noun2, attachment) -> None:
        ...
    
    def __repr__(self): # -> LiteralString:
        ...
    


class PPAttachmentCorpusReader(CorpusReader):
    """
    sentence_id verb noun1 preposition noun2 attachment
    """
    def attachments(self, fileids): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    
    def tuples(self, fileids): # -> str | ConcatenatedCorpusView | LazyConcatenation | list[Any] | tuple[()] | Element[str]:
        ...
    


