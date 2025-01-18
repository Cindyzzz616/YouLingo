import Video

A1 = 0.0
A2 = 1.0
B1 = 2.0
B2 = 3.0
C1 = 4.0
C2 = 5.0

class User:
    """
    A user.
    """

    id: int  # might not need it
    email: str  # get from Auth0
    password: str  # same here
    level: float
    topics: list[str]  # get from user input
    saved_videos: list[Video]
    native_language: str
    target_language: str # (if there's time)

    def __init__(self,
                 email: str,
                 password: str,
                 level: float,
                 topics: list[str],
                 native_language: str,
                 target_language: str) -> None:
        self.email = email
        self.password = password
        self.level = level
        self.topics = topics
        self.saved_videos = []
        self.native_language = native_language
        self.target_language = target_language

    def add_topic(self, topic: str) -> None:
        self.topics.append(topic)

    def save_video(self, video: Video) -> None:
        if video not in self.saved_videos:
            self.saved_videos.append(video)

    def remove_video_from_saved(self, video: Video) -> None:
        if video in self.saved_videos:
            self.saved_videos.remove(video)

    def increment_level(self) -> None:
        self.level += 0.1
