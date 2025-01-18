class Level:
    """
    The level of a user's language knowledge.
    """
    cefr: str

    def __init__(self, cefr: str):
        self.cefr: str = cefr
