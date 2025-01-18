from typing import List

from backend.Entities import Video

class FetchVideoInfo:
    """
    Return information to be displayed when a video is opened.
    """

    video: Video

    def __init__(self, video: Video, user: User) -> None:
        self.video = video

    def get_transcripts(self) -> List[(dict[str, str], dict[str, str] | None)] | str:
        # reformat the transcripts to be displayed?
        return self.video.transcripts


    def get_difficulty(self) -> int:
        """Returns the general difficulty level of the video as an integer."""
        return self.video.final_levels['general']

