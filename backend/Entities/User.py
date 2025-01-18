from typing import List

import Level
import Topic
import Video


class User:
    """
    A user.
    """

    id: int  # might not need it
    email: str  # get from Auth0
    password: str  # same here
    level: Level
    topics: List[Topic]  # get from user input; could also just be a list of str
    videos: List[Video]
    native_language: str  # or make a language object?
    # target_language: str (if there's time)

    def __init__(self):
        self.name = ''
