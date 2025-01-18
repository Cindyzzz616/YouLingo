from backend.Entities import Transcript


class Video:
    """
    A YouTube video.
    """

    url: str # might change to an url object later
    # other attributes based on api response...
    repetitions: int
    transcript: Transcript

    def __init__(self):
        self.url = ''
        repetitions = 0
