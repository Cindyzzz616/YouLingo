from moviepy import VideoFileClip

class Video:
    """
    Represents a video file with its path.
    """

    path: str
    length: float = -1.0  # Default value indicating length is unknown

    def __init__(self, path: str):
        self.path = path
        self.length = self.calculate_length()

    def calculate_length(self) -> float:
        """
        Calculate the length of the video in seconds.
        """
        clip = VideoFileClip(self.path)
        return clip.duration  # in seconds
