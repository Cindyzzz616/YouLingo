from backend.Entities import User, Video


class UpdateVideoStatus:
    """
    Update the status of a Video for the User.
    """

    video: Video
    user: User

    def __init__(self, video: Video, user: User) -> None:
        self.video = video
        self.user = user

    def save_video(self) -> None:
        # might be more complicated bc you need to update the database
        # should it return a bool to indicate whether the action was successful?
        self.user.saved_videos.append(self.video)
