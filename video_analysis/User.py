class User:
    """
    A class representing a user in a video analysis system.
    This class contains the vocabulary size and a lexicon of words.
    """

    vocab_size: int
    lexicon: list[str]

    def __init__(self, vocab_size, lexicon):
        self.vocab_size = vocab_size
        self.lexicon = lexicon