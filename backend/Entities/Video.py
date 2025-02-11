from youtube_transcript_api import YouTubeTranscriptApi
import requests

from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
CATHOVEN_CLIENT_ID = os.getenv("CATHOVEN_CLIENT_ID")
CATHOVEN_CLIENT_SECRET = os.getenv("CATHOVEN_CLIENT_SECRET")

YOUTUBE_URL="https://www.googleapis.com/youtube/v3/videos"
CATHOVEN_URL="https://enterpriseapi.cathoven.com/cefr/process_text"


class Video:
    """
    A YouTube video.
    """

    # attributes from youtube api response
    videoId: str
    title: str
    description: str
    duration: str
    thumbnails: dict[str, dict[str, int | str] | dict[str, int | str] | dict[str, int | str] | dict[str, int | str] | dict[str, int | str]]
    channelId: str
    channelTitle: str
    video_language: str


    # attributes from transcript api response
    original_transcript_list: list[dict[str, float | str]]
    original_transcript: dict[int, dict[str, float | str]]
    translated_transcript_list: list[dict[str, float]]
    translated_transcript: dict[int, dict[str, float | str]]

    transcript_text: str

    # attributes from cathoven api response
    final_levels: dict[str, float]
    wordlists: dict
    tenses: dict
    clauses: dict
    phrases: dict

    # other attributes
    native_language: str  # need to get this from user...

    def __init__(self, videoId: str, native_language: str) -> None:
        self.videoId = videoId
        self.native_language = native_language

        self.title = 'No title available'
        self.description = 'No description available'
        self.duration = 'No duration available'
        self.thumbnails = {'default': {'url': 'https://i.ytimg.com', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com', 'width': 1280, 'height': 720}}
        self.channelId = 'No channel ID available'
        self.channelTitle = 'No channel title available'
        self.video_language = 'en'
        self.original_transcript_list = [{'text': 'No English transcript available', 'start': 0.0, 'duration': 0.0}]
        self.translated_transcript_list = [{'text': "No translation for transcript available", 'start': 0.0, 'duration': 0.0}]
        self.original_transcript = {0: {'text': 'No English transcript available', 'start': 0.0, 'duration': 0.0}}
        self.translated_transcript = {0: {'text': "No translation for transcript available", 'start': 0.0, 'duration': 0.0}}

        self.final_levels = {'general': 0.0, 'vocab': 0.0, 'tense': 0.0, 'clause': 0.0}
        self.wordlists = {'-1.0': {'lemma': ['no wordlist available'], 'pos': ['N/A'], 'size': [0]}, '0.0': {'lemma': [], 'pos': [], 'size': []}, '1.0': {'lemma': [], 'pos': [], 'size': []}, '2.0': {'lemma': [], 'pos': [], 'size': []}, '3.0': {'lemma': [], 'pos': [], 'size': []}, '4.0': {'lemma': [], 'pos': [], 'size': []}, '5.0': {'lemma': [], 'pos': [], 'size': []}}
        self.tenses = {'No tenses available': {'form': ['N/A'], 'size': [1], 'tense': ['N/A'], 'level': [0.0], 'span': [[[0]]], 'sentence_id': [[1]]}}
        self.clauses = {'No clauses available': {'clause_form': ['N/A'], 'size': [1], 'clause_span': [[0]], 'sentence_id': [[0]]}}

        self.transcript_text = 'No transcript available'



    def add_video_details(self) -> str | None:
        params = {
            'part': 'snippet,contentDetails,statistics',
            'id': self.videoId,
            'key': YOUTUBE_API_KEY
        }
        response = requests.get(YOUTUBE_URL, params=params)
        response.raise_for_status()  # Raise error if request failed
        data = response.json()

        if data['items']:
            video = data['items'][0]
            self.title = video['snippet']['title']
            self.description = video['snippet']['description']
            self.duration = video['contentDetails']['duration']
            self.thumbnails = video['snippet']['thumbnails']  # Correctly access the thumbnails field
            self.channelId = video['snippet']['channelId']
            self.channelTitle = video['snippet']['channelTitle']
            self.video_language = video['snippet'].get('defaultLanguage', 'en')  # Provide a default value if not present
        else:
            return 'Video not found'

    def add_transcripts(self) -> str | None:
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(self.videoId)
            for transcript in transcript_list:
                if transcript.language_code == 'en':
                    self.original_transcript_list = transcript.fetch()
                    i = 0
                    for line in self.original_transcript_list:
                        self.original_transcript[i] = line
                        i += 1
                if transcript.is_translatable:
                    self.translated_transcript_list = transcript.translate(self.native_language).fetch()
                    i = 0
                    for line in self.translated_transcript_list:
                        self.translated_transcript[i] = line
                        i += 1
        except Exception as e:
            return f"Error: {str(e)}"

    def add_difficulty(self) -> str | None:
        if not self.original_transcript or self.original_transcript == {0: {'text': 'No English transcript available', 'start': 0.0, 'duration': 0.0}}:
            return 'No transcript available'
        else:
            self.transcript_text = ''
            word_count = 0
            for line in self.original_transcript_list:
                word_count += len(line['text'].split(' '))
                if word_count < 500:
                    self.transcript_text = self.transcript_text + line['text'] + ' '
                else:
                    break


            payload = {
                'client_id': CATHOVEN_CLIENT_ID,
                'client_secret': CATHOVEN_CLIENT_SECRET,
                'text': self.transcript_text,
                'v': 2,  # Version of the CEFR Analyser
                'propn_as_lowest': True,
                'intj_as_lowest': True,
                'keep_min': True,
                'custom_dictionary': {},  # Add custom vocabulary levels if needed
                'return_final_levels': True,
                "outputs": [
                    "wordlists",
                    "tense_term_count",
                    "clause_count",
                    "final_levels"
                ]
                # somehow "phrase_count" is not in the list of allowed output params - we'll have to see what happens
                # removed sentences, vocabulary_stats, tense_count, tense_stats, clause_stats
            }

            response = requests.post(CATHOVEN_URL, data=payload)

            if response.status_code == 200:
                analysis_result = response.json()
                self.final_levels = analysis_result['final_levels']
                self.wordlists = analysis_result['wordlists']
                self.tenses = analysis_result['tense_term_count']
                self.clauses = analysis_result['clause_count']
                # self.allowed_remaining = analysis_result['allowed_remaining']
                # self.phrases = analysis_result.get('phrase_count', {})  # Handle absence of phrase_count
            else:
                return f'Error: {response.status_code}'
