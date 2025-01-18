from backend.Entities import User, Video


COMPLETION_THRESHOLD = 10


class UpdateUserLevel:
    """
    Check whether the video is completed after a viewing event; if so,
    increment the level of the user.
    """

    user: User

    def __init__(self, user: User):
        self.user = user

    def update(self, video: Video):
        if not video.completion and video.view_count >= COMPLETION_THRESHOLD:
            video.completion = True
            self.user.increment_level()
            # also notify the user
