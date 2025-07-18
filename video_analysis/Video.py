class Video:
    """
    Represents a video file with its path.
    """

    path: str
    
    def __init__(self, path: str):
        self.path = path