"""
This type stub file was generated by pyright.
"""

"""
Common methods and classes for all IBM models. See ``IBMModel1``,
``IBMModel2``, ``IBMModel3``, ``IBMModel4``, and ``IBMModel5``
for specific implementations.

The IBM models are a series of generative models that learn lexical
translation probabilities, p(target language word|source language word),
given a sentence-aligned parallel corpus.

The models increase in sophistication from model 1 to 5. Typically, the
output of lower models is used to seed the higher models. All models
use the Expectation-Maximization (EM) algorithm to learn various
probability tables.

Words in a sentence are one-indexed. The first word of a sentence has
position 1, not 0. Index 0 is reserved in the source sentence for the
NULL token. The concept of position does not apply to NULL, but it is
indexed at 0 by convention.

Each target word is aligned to exactly one source word or the NULL
token.

References:
Philipp Koehn. 2010. Statistical Machine Translation.
Cambridge University Press, New York.

Peter E Brown, Stephen A. Della Pietra, Vincent J. Della Pietra, and
Robert L. Mercer. 1993. The Mathematics of Statistical Machine
Translation: Parameter Estimation. Computational Linguistics, 19 (2),
263-311.
"""
def longest_target_sentence_length(sentence_aligned_corpus): # -> int:
    """
    :param sentence_aligned_corpus: Parallel corpus under consideration
    :type sentence_aligned_corpus: list(AlignedSent)
    :return: Number of words in the longest target language sentence
        of ``sentence_aligned_corpus``
    """
    ...

class IBMModel:
    """
    Abstract base class for all IBM models
    """
    MIN_PROB = ...
    def __init__(self, sentence_aligned_corpus) -> None:
        ...
    
    def reset_probabilities(self): # -> None:
        ...
    
    def set_uniform_probabilities(self, sentence_aligned_corpus): # -> None:
        """
        Initialize probability tables to a uniform distribution

        Derived classes should implement this accordingly.
        """
        ...
    
    def init_vocab(self, sentence_aligned_corpus): # -> None:
        ...
    
    def sample(self, sentence_pair): # -> tuple[set[Any], AlignmentInfo | Any]:
        """
        Sample the most probable alignments from the entire alignment
        space

        First, determine the best alignment according to IBM Model 2.
        With this initial alignment, use hill climbing to determine the
        best alignment according to a higher IBM Model. Add this
        alignment and its neighbors to the sample set. Repeat this
        process with other initial alignments obtained by pegging an
        alignment point.

        Hill climbing may be stuck in a local maxima, hence the pegging
        and trying out of different alignments.

        :param sentence_pair: Source and target language sentence pair
            to generate a sample of alignments from
        :type sentence_pair: AlignedSent

        :return: A set of best alignments represented by their ``AlignmentInfo``
            and the best alignment of the set for convenience
        :rtype: set(AlignmentInfo), AlignmentInfo
        """
        ...
    
    def best_model2_alignment(self, sentence_pair, j_pegged=..., i_pegged=...): # -> AlignmentInfo:
        """
        Finds the best alignment according to IBM Model 2

        Used as a starting point for hill climbing in Models 3 and
        above, because it is easier to compute than the best alignments
        in higher models

        :param sentence_pair: Source and target language sentence pair
            to be word-aligned
        :type sentence_pair: AlignedSent

        :param j_pegged: If specified, the alignment point of j_pegged
            will be fixed to i_pegged
        :type j_pegged: int

        :param i_pegged: Alignment point to j_pegged
        :type i_pegged: int
        """
        ...
    
    def hillclimb(self, alignment_info, j_pegged=...):
        """
        Starting from the alignment in ``alignment_info``, look at
        neighboring alignments iteratively for the best one

        There is no guarantee that the best alignment in the alignment
        space will be found, because the algorithm might be stuck in a
        local maximum.

        :param j_pegged: If specified, the search will be constrained to
            alignments where ``j_pegged`` remains unchanged
        :type j_pegged: int

        :return: The best alignment found from hill climbing
        :rtype: AlignmentInfo
        """
        ...
    
    def neighboring(self, alignment_info, j_pegged=...): # -> set[Any]:
        """
        Determine the neighbors of ``alignment_info``, obtained by
        moving or swapping one alignment point

        :param j_pegged: If specified, neighbors that have a different
            alignment point from j_pegged will not be considered
        :type j_pegged: int

        :return: A set neighboring alignments represented by their
            ``AlignmentInfo``
        :rtype: set(AlignmentInfo)
        """
        ...
    
    def maximize_lexical_translation_probabilities(self, counts): # -> None:
        ...
    
    def maximize_fertility_probabilities(self, counts): # -> None:
        ...
    
    def maximize_null_generation_probabilities(self, counts): # -> None:
        ...
    
    def prob_of_alignments(self, alignments): # -> float | Literal[0]:
        ...
    
    def prob_t_a_given_s(self, alignment_info): # -> float:
        """
        Probability of target sentence and an alignment given the
        source sentence

        All required information is assumed to be in ``alignment_info``
        and self.

        Derived classes should override this method
        """
        ...
    


class AlignmentInfo:
    """
    Helper data object for training IBM Models 3 and up

    Read-only. For a source sentence and its counterpart in the target
    language, this class holds information about the sentence pair's
    alignment, cepts, and fertility.

    Warning: Alignments are one-indexed here, in contrast to
    nltk.translate.Alignment and AlignedSent, which are zero-indexed
    This class is not meant to be used outside of IBM models.
    """
    def __init__(self, alignment, src_sentence, trg_sentence, cepts) -> None:
        ...
    
    def fertility_of_i(self, i): # -> int:
        """
        Fertility of word in position ``i`` of the source sentence
        """
        ...
    
    def is_head_word(self, j):
        """
        :return: Whether the word in position ``j`` of the target
            sentence is a head word
        """
        ...
    
    def center_of_cept(self, i): # -> int:
        """
        :return: The ceiling of the average positions of the words in
            the tablet of cept ``i``, or 0 if ``i`` is None
        """
        ...
    
    def previous_cept(self, j): # -> None:
        """
        :return: The previous cept of ``j``, or None if ``j`` belongs to
            the first cept
        """
        ...
    
    def previous_in_tablet(self, j): # -> None:
        """
        :return: The position of the previous word that is in the same
            tablet as ``j``, or None if ``j`` is the first word of the
            tablet
        """
        ...
    
    def zero_indexed_alignment(self): # -> list[Any]:
        """
        :return: Zero-indexed alignment, suitable for use in external
            ``nltk.translate`` modules like ``nltk.translate.Alignment``
        :rtype: list(tuple)
        """
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class Counts:
    """
    Data object to store counts of various parameters during training
    """
    def __init__(self) -> None:
        ...
    
    def update_lexical_translation(self, count, alignment_info, j): # -> None:
        ...
    
    def update_null_generation(self, count, alignment_info): # -> None:
        ...
    
    def update_fertility(self, count, alignment_info): # -> None:
        ...
    


