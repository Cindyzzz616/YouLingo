from typing import List

import Level
import Topic
import Video


class User:
    """
    A user.
    """

    id: int  # might not need it
    email: str
    level: Level
    topics: List[Topic]
    videos: List[Video]
    native_language: str  # or make a language object?
    # target_language: str (if there's time)

    def __init__(self):
        self.name = ''
