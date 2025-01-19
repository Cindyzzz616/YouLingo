import requests
import random
import isodate
from dotenv import load_dotenv
import os

from backend.Entities import User

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

# can make customizable in the future
DIFFICULTY_RANGE = 0.5
MAX_DURATION = 240.0


class FetchVideoBatch:
    """
    Fetch a batch of videos based on the user's topics of interest or search query.
    """

    user: User

    def __init__(self, user: User):
        self.user = user

    # this doesn't filter by difficulty yet
    def fetch_searched_videos(self, query: str, max_results: int) -> list[dict]:
        batch = None
        params = {
            'part': 'snippet',
            'type': 'video',
            'q': query,
            'maxResults': max_results,
            'key': API_KEY
        }

        try:
            response = requests.get(SEARCH_URL, params=params)
            response.raise_for_status()
            data = response.json()
            batch = data.get('items', [])
            print(batch)  # for testing
        except requests.exceptions.RequestException as e:
            print(f'Error fetching videos: {e}')

        return batch

    def fetch_recommended_videos(self) -> list[dict]:
        batch = []
        randomized_topics = random.sample(self.user.topics, 10)
        for topic in randomized_topics:
            need_new_video = True
            while need_new_video:
                video = self.fetch_searched_videos(topic, 1)[0]
                video_obj = Video.Video(video['id'], self.user.native_language)
                video_obj.add_video_details()
                video_obj.add_transcripts()
                video_obj.add_difficulty()
                duration_in_seconds = isodate.parse_duration(video_obj.duration).total_seconds()
                if abs(video_obj.final_levels['general'] - self.user.level) < DIFFICULTY_RANGE \
                        and video_obj.video_language == 'en' \
                        and duration_in_seconds < MAX_DURATION:
                    batch.append(self.fetch_searched_videos(topic, 1)[0])
                    need_new_video = False
        return batch
