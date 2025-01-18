from typing import List

import Level
import Topic
import Video


class User:
    """
    A user.
    """

    name: str
    level: Level
    topics: List[Topic]
    videos: List[Video]

    def __init__(self):
        self.name = ''
