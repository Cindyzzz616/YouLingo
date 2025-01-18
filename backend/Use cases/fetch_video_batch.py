import requests
import random

from backend.Entities import User, Video

API_KEY = 'AIzaSyBT2UKWCmrb9DcK_OLGSegbkd8WDE3-XBI'
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

class FetchVideoBatch:
    """
    Fetch a batch of recommended videos based on the user's topics of interest.
    """

    user: User
    # api info...
    # also need to know how many videos to fetch - should we predetermine that?

    def __init__(self, user: User):
        self.user = user

    def fetch_searched_videos(self, query: str, max_results: int) -> list[dict]:
        # or not take in a query but get it from self.user?
        # make this return a list of Videos instead? whichever is easier to use
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

    # TODO right now this only fetches the videos by topic - also need to filter by difficulty!
    def fetch_recommended_videos(self) -> list[dict]:
        batch = []
        randomized_topics = random.sample(self.user.topics, 10)
        for topic in randomized_topics:
            video = self.fetch_searched_videos(topic, 1)[0]
            # if video lang is right:
            batch.append(self.fetch_searched_videos(topic, 1)[0])
        return batch
