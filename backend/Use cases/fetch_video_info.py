from backend.Entities import Video


class FetchVideoInfo:
    """
    Return information to be displayed when a video is opened.
    """

    video: Video

    def __init__(self, video: Video) -> None:
        self.video = video

    def get_transcript(self) -> str:
        # temporary return - should probably have a getter for transcript
        # should we call the transcript api here or in the video entity? probably here?
        # since the number of calls to the transcript api is limited, we should only call it when a video
        # is clicked on (not when a batch of video is displayed)
        return self.video.transcript

    def get_video_info(self) -> dict:
        # gotta figure out the return type
        transcript = self.get_transcript
        return
