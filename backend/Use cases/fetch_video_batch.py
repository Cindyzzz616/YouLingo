from typing import List

from backend.Entities import User, Video


class FetchVideoBatch:
    """
    Fetch a batch of recommended videos based on the user's topics of interest.
    """

    user: User
    # api info...
    # also need to know how many videos to fetch - should we predetermine that?

    def __init__(self, user: User):
        self.user = user

    def fetch_video_batch(self) -> List[Video]:
        batch = []
        # add videos to batch using youtube api...
        return batch
        
