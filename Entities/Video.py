class Video:
    """
    A YouTube video.
    """

    url: str # might change to an url object later
    # other attributes based on api response...
    repetitions: int

    def __init__(self):
        self.url = ''
        repetitions = 0
