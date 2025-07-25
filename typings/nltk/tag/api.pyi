"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod
from typing import Dict
from nltk.internals import deprecated

"""
Interface for tagging each token in a sentence with supplementary
information, such as its part of speech.
"""
class TaggerI(metaclass=ABCMeta):
    """
    A processing interface for assigning a tag to each token in a list.
    Tags are case sensitive strings that identify some property of each
    token, such as its part of speech or its sense.

    Some taggers require specific types for their tokens.  This is
    generally indicated by the use of a sub-interface to ``TaggerI``.
    For example, featureset taggers, which are subclassed from
    ``FeaturesetTagger``, require that each token be a ``featureset``.

    Subclasses must define:
      - either ``tag()`` or ``tag_sents()`` (or both)
    """
    @abstractmethod
    def tag(self, tokens): # -> None:
        """
        Determine the most appropriate tag sequence for the given
        token sequence, and return a corresponding list of tagged
        tokens.  A tagged token is encoded as a tuple ``(token, tag)``.

        :rtype: list(tuple(str, str))
        """
        ...
    
    def tag_sents(self, sentences): # -> list[Any | None]:
        """
        Apply ``self.tag()`` to each element of *sentences*.  I.e.::

            return [self.tag(sent) for sent in sentences]
        """
        ...
    
    @deprecated("Use accuracy(gold) instead.")
    def evaluate(self, gold): # -> float:
        ...
    
    def accuracy(self, gold): # -> float:
        """
        Score the accuracy of the tagger against the gold standard.
        Strip the tags from the gold standard text, retag it using
        the tagger, then compute the accuracy score.

        :param gold: The list of tagged sentences to score the tagger on.
        :type gold: list(list(tuple(str, str)))
        :rtype: float
        """
        ...
    
    def confusion(self, gold): # -> ConfusionMatrix:
        """
        Return a ConfusionMatrix with the tags from ``gold`` as the reference
        values, with the predictions from ``tag_sents`` as the predicted values.

        >>> from nltk.tag import PerceptronTagger
        >>> from nltk.corpus import treebank
        >>> tagger = PerceptronTagger()
        >>> gold_data = treebank.tagged_sents()[:10]
        >>> print(tagger.confusion(gold_data))
               |        -                                                                                     |
               |        N                                                                                     |
               |        O                                               P                                     |
               |        N                       J  J        N  N  P  P  R     R           V  V  V  V  V  W    |
               |  '     E     C  C  D  E  I  J  J  J  M  N  N  N  O  R  P  R  B  R  T  V  B  B  B  B  B  D  ` |
               |  '  ,  -  .  C  D  T  X  N  J  R  S  D  N  P  S  S  P  $  B  R  P  O  B  D  G  N  P  Z  T  ` |
        -------+----------------------------------------------------------------------------------------------+
            '' | <1> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
             , |  .<15> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
        -NONE- |  .  . <.> .  .  2  .  .  .  2  .  .  .  5  1  .  .  .  .  2  .  .  .  .  .  .  .  .  .  .  . |
             . |  .  .  .<10> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
            CC |  .  .  .  . <1> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
            CD |  .  .  .  .  . <5> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
            DT |  .  .  .  .  .  .<20> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
            EX |  .  .  .  .  .  .  . <1> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
            IN |  .  .  .  .  .  .  .  .<22> .  .  .  .  .  .  .  .  .  .  3  .  .  .  .  .  .  .  .  .  .  . |
            JJ |  .  .  .  .  .  .  .  .  .<16> .  .  .  .  1  .  .  .  .  1  .  .  .  .  .  .  .  .  .  .  . |
           JJR |  .  .  .  .  .  .  .  .  .  . <.> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
           JJS |  .  .  .  .  .  .  .  .  .  .  . <1> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
            MD |  .  .  .  .  .  .  .  .  .  .  .  . <1> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
            NN |  .  .  .  .  .  .  .  .  .  .  .  .  .<28> 1  1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
           NNP |  .  .  .  .  .  .  .  .  .  .  .  .  .  .<25> .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
           NNS |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .<19> .  .  .  .  .  .  .  .  .  .  .  .  .  .  . |
           POS |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <1> .  .  .  .  .  .  .  .  .  .  .  .  .  . |
           PRP |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <4> .  .  .  .  .  .  .  .  .  .  .  .  . |
          PRP$ |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <2> .  .  .  .  .  .  .  .  .  .  .  . |
            RB |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <4> .  .  .  .  .  .  .  .  .  .  . |
           RBR |  .  .  .  .  .  .  .  .  .  .  1  .  .  .  .  .  .  .  .  . <1> .  .  .  .  .  .  .  .  .  . |
            RP |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <1> .  .  .  .  .  .  .  .  . |
            TO |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <5> .  .  .  .  .  .  .  . |
            VB |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <3> .  .  .  .  .  .  . |
           VBD |  .  .  .  .  .  .  .  .  .  .  .  .  .  1  .  .  .  .  .  .  .  .  .  . <6> .  .  .  .  .  . |
           VBG |  .  .  .  .  .  .  .  .  .  .  .  .  .  1  .  .  .  .  .  .  .  .  .  .  . <4> .  .  .  .  . |
           VBN |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  . <4> .  .  .  . |
           VBP |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <3> .  .  . |
           VBZ |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <7> .  . |
           WDT |  .  .  .  .  .  .  .  .  2  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <.> . |
            `` |  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . <1>|
        -------+----------------------------------------------------------------------------------------------+
        (row = reference; col = test)
        <BLANKLINE>

        :param gold: The list of tagged sentences to run the tagger with,
            also used as the reference values in the generated confusion matrix.
        :type gold: list(list(tuple(str, str)))
        :rtype: ConfusionMatrix
        """
        ...
    
    def recall(self, gold) -> Dict[str, float]:
        """
        Compute the recall for each tag from ``gold`` or from running ``tag``
        on the tokenized sentences from ``gold``. Then, return the dictionary
        with mappings from tag to recall. The recall is defined as:

        - *r* = true positive / (true positive + false positive)

        :param gold: The list of tagged sentences to score the tagger on.
        :type gold: list(list(tuple(str, str)))
        :return: A mapping from tags to recall
        :rtype: Dict[str, float]
        """
        ...
    
    def precision(self, gold): # -> dict[Any, float]:
        """
        Compute the precision for each tag from ``gold`` or from running ``tag``
        on the tokenized sentences from ``gold``. Then, return the dictionary
        with mappings from tag to precision. The precision is defined as:

        - *p* = true positive / (true positive + false negative)

        :param gold: The list of tagged sentences to score the tagger on.
        :type gold: list(list(tuple(str, str)))
        :return: A mapping from tags to precision
        :rtype: Dict[str, float]
        """
        ...
    
    def f_measure(self, gold, alpha=...): # -> dict[Any, float]:
        """
        Compute the f-measure for each tag from ``gold`` or from running ``tag``
        on the tokenized sentences from ``gold``. Then, return the dictionary
        with mappings from tag to f-measure. The f-measure is the harmonic mean
        of the ``precision`` and ``recall``, weighted by ``alpha``.
        In particular, given the precision *p* and recall *r* defined by:

        - *p* = true positive / (true positive + false negative)
        - *r* = true positive / (true positive + false positive)

        The f-measure is:

        - *1/(alpha/p + (1-alpha)/r)*

        With ``alpha = 0.5``, this reduces to:

        - *2pr / (p + r)*

        :param gold: The list of tagged sentences to score the tagger on.
        :type gold: list(list(tuple(str, str)))
        :param alpha: Ratio of the cost of false negative compared to false
            positives. Defaults to 0.5, where the costs are equal.
        :type alpha: float
        :return: A mapping from tags to precision
        :rtype: Dict[str, float]
        """
        ...
    
    def evaluate_per_tag(self, gold, alpha=..., truncate=..., sort_by_count=...): # -> LiteralString | str:
        """Tabulate the **recall**, **precision** and **f-measure**
        for each tag from ``gold`` or from running ``tag`` on the tokenized
        sentences from ``gold``.

        >>> from nltk.tag import PerceptronTagger
        >>> from nltk.corpus import treebank
        >>> tagger = PerceptronTagger()
        >>> gold_data = treebank.tagged_sents()[:10]
        >>> print(tagger.evaluate_per_tag(gold_data))
           Tag | Prec.  | Recall | F-measure
        -------+--------+--------+-----------
            '' | 1.0000 | 1.0000 | 1.0000
             , | 1.0000 | 1.0000 | 1.0000
        -NONE- | 0.0000 | 0.0000 | 0.0000
             . | 1.0000 | 1.0000 | 1.0000
            CC | 1.0000 | 1.0000 | 1.0000
            CD | 0.7143 | 1.0000 | 0.8333
            DT | 1.0000 | 1.0000 | 1.0000
            EX | 1.0000 | 1.0000 | 1.0000
            IN | 0.9167 | 0.8800 | 0.8980
            JJ | 0.8889 | 0.8889 | 0.8889
           JJR | 0.0000 | 0.0000 | 0.0000
           JJS | 1.0000 | 1.0000 | 1.0000
            MD | 1.0000 | 1.0000 | 1.0000
            NN | 0.8000 | 0.9333 | 0.8615
           NNP | 0.8929 | 1.0000 | 0.9434
           NNS | 0.9500 | 1.0000 | 0.9744
           POS | 1.0000 | 1.0000 | 1.0000
           PRP | 1.0000 | 1.0000 | 1.0000
          PRP$ | 1.0000 | 1.0000 | 1.0000
            RB | 0.4000 | 1.0000 | 0.5714
           RBR | 1.0000 | 0.5000 | 0.6667
            RP | 1.0000 | 1.0000 | 1.0000
            TO | 1.0000 | 1.0000 | 1.0000
            VB | 1.0000 | 1.0000 | 1.0000
           VBD | 0.8571 | 0.8571 | 0.8571
           VBG | 1.0000 | 0.8000 | 0.8889
           VBN | 1.0000 | 0.8000 | 0.8889
           VBP | 1.0000 | 1.0000 | 1.0000
           VBZ | 1.0000 | 1.0000 | 1.0000
           WDT | 0.0000 | 0.0000 | 0.0000
            `` | 1.0000 | 1.0000 | 1.0000
        <BLANKLINE>

        :param gold: The list of tagged sentences to score the tagger on.
        :type gold: list(list(tuple(str, str)))
        :param alpha: Ratio of the cost of false negative compared to false
            positives, as used in the f-measure computation. Defaults to 0.5,
            where the costs are equal.
        :type alpha: float
        :param truncate: If specified, then only show the specified
            number of values.  Any sorting (e.g., sort_by_count)
            will be performed before truncation. Defaults to None
        :type truncate: int, optional
        :param sort_by_count: Whether to sort the outputs on number of
            occurrences of that tag in the ``gold`` data, defaults to False
        :type sort_by_count: bool, optional
        :return: A tabulated recall, precision and f-measure string
        :rtype: str
        """
        ...
    


class FeaturesetTaggerI(TaggerI):
    """
    A tagger that requires tokens to be ``featuresets``.  A featureset
    is a dictionary that maps from feature names to feature
    values.  See ``nltk.classify`` for more information about features
    and featuresets.
    """
    ...


