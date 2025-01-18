from youtube_transcript_api import YouTubeTranscriptApi
import requests

YOUTUBE_API_KEY = 'AIzaSyBT2UKWCmrb9DcK_OLGSegbkd8WDE3-XBI'
YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/videos'

CATHOVEN_URL = 'https://enterpriseapi.cathoven.com/cefr/process_text'
CATHOVEN_CLIENT_ID = '41b95a1e-89cf-4194-ad44-da6a542da143'
CATHOVEN_CLIENT_SECRET = '313f758a-a846-4e25-8656-b80e012f7216'


class Video:
    """
    A YouTube video.
    """

    # attributes from youtube api response
    videoId: str
    title: str
    description: str
    duration: str
    thumbnails: dict[str, str | int]  # will have to see how this works
    # do we need these?
    channelId: str
    channelTitle: str
    video_language: str


    # attributes from transcript api response
    transcripts: list[(list[dict[str, float | str]], list[dict[str, float | str]])]
    # a tuple of transcript and translated transcript
    # TODO change the data type ^

    # attributes from cathoven api response
    final_levels: dict[str, float]
    wordlists: dict
    tenses: dict
    clauses: dict
    phrases: dict

    # sentences - might be useful bc it gives the difficulty breakdown of each word in a sentence

    # other attributes
    native_language: str  # need to get this from user...

    def __init__(self, videoId: str, native_language: str) -> None:
        self.videoId = videoId
        self.native_language = native_language
        self.transcripts = []

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
                transcript_data = transcript.fetch()
                if transcript.is_translatable:
                    transcript_translated = transcript.translate(self.native_language).fetch()
                else:
                    transcript_translated = None
                self.transcripts.append((transcript_data, transcript_translated))
        except Exception as e:
            return f"Error: {str(e)}"

    def add_difficulty(self) -> str | None:
        if not self.transcripts:
            self.add_transcripts()

        # for now, we just analyze the first available transcript. We can allow user to choose a transcript later on

        transcript_text = ''
        for line in self.transcripts[0][0]:
            transcript_text = transcript_text + line['text'] + '. '

        payload = {
            'client_id': CATHOVEN_CLIENT_ID,
            'client_secret': CATHOVEN_CLIENT_SECRET,
            'text': transcript_text,
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
            self.phrases = analysis_result['phrase_count']  # might not exist
        else:
            return f'Error: {response.status_code}'
