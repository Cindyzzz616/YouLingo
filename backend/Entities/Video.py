import os

from youtube_transcript_api import YouTubeTranscriptApi
import requests

YOUTUBE_API_KEY="AIzaSyBT2UKWCmrb9DcK_OLGSegbkd8WDE3-XBI"
YOUTUBE_URL="https://www.googleapis.com/youtube/v3/videos"

CATHOVEN_URL="https://enterpriseapi.cathoven.com/cefr/process_text"
CATHOVEN_CLIENT_ID="41b95a1e-89cf-4194-ad44-da6a542da143"
CATHOVEN_CLIENT_SECRET="313f758a-a846-4e25-8656-b80e012f7216"

# YOUTUBE_API_KEY=os.getenv("YOUTUBE_API_KEY")
# if not YOUTUBE_API_KEY:
#     raise ValueError("API_KEY not found in environment variables!")
#
# YOUTUBE_URL="https://www.googleapis.com/youtube/v3/videos"
#
# CATHOVEN_URL="https://enterpriseapi.cathoven.com/cefr/process_text"
# CATHOVEN_CLIENT_ID="41b95a1e-89cf-4194-ad44-da6a542da143"
# CATHOVEN_CLIENT_SECRET="313f758a-a846-4e25-8656-b80e012f7216"

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
    # thumbnails: dict[str, str | int]  # will have to see how this works
    # do we need these?
    channelId: str
    channelTitle: str
    video_language: str


    # attributes from transcript api response
    # transcripts: list[(list[dict[str, float | str]], list[dict[str, float | str]])]
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

    # allowed_remaining: dict

    # sentences - might be useful bc it gives the difficulty breakdown of each word in a sentence

    # other attributes
    native_language: str  # need to get this from user...

    def __init__(self, videoId: str, native_language: str) -> None:
        self.videoId = videoId
        self.native_language = native_language

        self.title = 'No title available'
        self.description = 'No description available'
        self.duration = 'No duration available'
        self.thumbnails = {'default': {'url': 'https://i.ytimg.com/vi/Zp-Jhuhq0bQ/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/Zp-Jhuhq0bQ/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/Zp-Jhuhq0bQ/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/Zp-Jhuhq0bQ/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/Zp-Jhuhq0bQ/maxresdefault.jpg', 'width': 1280, 'height': 720}}
        self.channelId = 'No channel ID available'
        self.channelTitle = 'No channel title available'
        self.video_language = 'en'
        self.original_transcript_list = [{'text': 'the most valuable commodity I know of is',
                                          'start': 0.919, 'duration': 6.571}]
        self.translated_transcript_list = [{'text': "le bien le plus précieux que je connaisse est l'", 'start': 0.919, 'duration': 6.571}]
        self.original_transcript = {
            0: {'text': 'the most valuable commodity I know of is',
                'start': 0.919, 'duration': 6.571}}
        self.translated_transcript = {0: {'text': "le bien le plus précieux "
                                                  "que je connaisse est l'",
                                          'start': 0.919, 'duration': 6.571}}

        self.final_levels = {'general': 0.0, 'vocab': 0.0, 'tense': 0.0, 'clause': 0.0}
        self.wordlists = {'-1.0': {'lemma': ['air', 'burn', 'desert', 'george', 'um'], 'pos': ['PROPN', 'PROPN', 'PROPN', 'PROPN', 'INTJ'], 'size': [1, 1, 1, 1, 1]}, '0.0': {'lemma': ['you', 'be', 'to', 'of', 'do', 'a', 'it', 'your', 'not', 'the', 'how', 'and', 'about', 'in', 'or', 'to', 'do', 'get', 'have', 'take', 'because', 'find', 'on', 'something', 'time', 'we', 'I', 'can', 'day', 'feel', 'go', 'life', 'many', 'old', 'say', 'their', 'they', 'us', 'into', 'job', 'kind', 'know', 'make', 'many', 'never', 'people', 'person', 'some', 'with', 'all', 'as', 'before', 'begin', 'body', 'but', 'cold', 'come', 'flower', 'food', 'for', 'from', 'give', 'good', 'he', 'hear', 'help', 'hour', 'its', 'key', 'most', 'music', 'now', 'our', 'out', 'talk', 'that', 'them', 'this', 'very', 'want', 'watch', 'what', 'where', 'world', 'would'], 'pos': ['PRON', 'AUX', 'PART', 'ADP', 'AUX', 'DET', 'PRON', 'PRON', 'ADV', 'DET', 'CONJ', 'CONJ', 'ADP', 'ADP', 'CONJ', 'ADP', 'VERB', 'VERB', 'VERB', 'VERB', 'CONJ', 'VERB', 'ADP', 'PRON', 'NOUN', 'PRON', 'PRON', 'AUX', 'NOUN', 'VERB', 'VERB', 'NOUN', 'ADJ', 'ADJ', 'VERB', 'PRON', 'PRON', 'PRON', 'ADP', 'NOUN', 'NOUN', 'VERB', 'VERB', 'DET', 'ADV', 'NOUN', 'NOUN', 'DET', 'ADP', 'PRON', 'ADP', 'ADP', 'VERB', 'NOUN', 'CONJ', 'ADJ', 'VERB', 'NOUN', 'NOUN', 'ADP', 'ADP', 'VERB', 'ADJ', 'PRON', 'VERB', 'VERB', 'NOUN', 'PRON', 'NOUN', 'ADV', 'X', 'ADV', 'PRON', 'ADP', 'VERB', 'DET', 'PRON', 'PRON', 'ADV', 'VERB', 'VERB', 'DET', 'CONJ', 'NOUN', 'AUX'], 'size': [33, 24, 20, 19, 15, 12, 12, 12, 11, 11, 8, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, '1.0': {'lemma': ['that', 'yourself', 'have', 'that', 'believe', 'bring', 'health', 'ourselves', 'term', 'themselves', 'which', 'agree', 'american', 'ask', 'build', 'if', 'in', 'information', 'just', 'let', 'level', 'mean', 'once', 'out', 'push', 'so', 'someone', 'sort', 'spend', 'through', 'unhappy', 'up'], 'pos': ['PRON', 'PRON', 'AUX', 'CONJ', 'VERB', 'VERB', 'NOUN', 'PRON', 'NOUN', 'PRON', 'PRON', 'VERB', 'ADJ', 'VERB', 'VERB', 'CONJ', 'ADV', 'NOUN', 'ADV', 'VERB', 'NOUN', 'VERB', 'ADV', 'ADV', 'VERB', 'CONJ', 'PRON', 'NOUN', 'VERB', 'ADP', 'ADJ', 'ADP'], 'size': [13, 7, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, '2.0': {'lemma': ['what', 'care', 'relationship', 'achieve', 'action', 'allow', 'appearance', 'attitude', 'career', 'challenging', 'chance', 'direction', 'effort', 'environment', 'exercise', 'involve', 'lack', 'poem', 'public', 'satisfied', 'sense', 'shape', 'talent', 'talented', 'touch', 'translate', 'universe', 'valuable', 'waste'], 'pos': ['PRON', 'NOUN', 'NOUN', 'VERB', 'NOUN', 'VERB', 'NOUN', 'NOUN', 'NOUN', 'ADJ', 'NOUN', 'NOUN', 'NOUN', 'NOUN', 'VERB', 'VERB', 'NOUN', 'NOUN', 'NOUN', 'ADJ', 'NOUN', 'NOUN', 'NOUN', 'ADJ', 'NOUN', 'VERB', 'NOUN', 'ADJ', 'VERB'], 'size': [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, '3.0': {'lemma': ['motivation', 'scale', 'mentally', 'simply', 'worthwhile', 'affect', 'challenge', 'conscious', 'contribution', 'define', 'deliberate', 'demonstrate', 'desirable', 'desire', 'expose', 'express', 'greatness', 'impact', 'inspire', 'measure', 'mental', 'motivated', 'overweight', 'physical', 'stimulate', 'stretch', 'toxic', 'upon'], 'pos': ['NOUN', 'NOUN', 'ADV', 'ADV', 'ADJ', 'VERB', 'VERB', 'ADJ', 'NOUN', 'VERB', 'ADJ', 'VERB', 'ADJ', 'NOUN', 'VERB', 'VERB', 'NOUN', 'NOUN', 'VERB', 'VERB', 'ADJ', 'ADJ', 'ADJ', 'ADJ', 'VERB', 'VERB', 'ADJ', 'CONJ'], 'size': [6, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, '4.0': {'lemma': ['rate', 'commodity', 'evaluate', 'fulfillment', 'motivate', 'self', 'unnoticed'], 'pos': ['VERB', 'NOUN', 'VERB', 'NOUN', 'VERB', 'NOUN', 'ADJ'], 'size': [2, 1, 1, 1, 1, 1, 1]}, '5.0': {'lemma': ['bloom', 'drain', 'indicator', 'nourish', 'sweetness', 'unceasingly'], 'pos': ['VERB', 'VERB', 'NOUN', 'VERB', 'NOUN', 'ADV'], 'size': [1, 1, 1, 1, 1, 1]}}
        self.tenses = {'Gerund simple': {'form': ['doing'], 'size': [3], 'tense': ['do_ger.'], 'level': [1.0], 'span': [[[63], [305], [395]]], 'sentence_id': [[1, 2, 2]]}, 'Imperative': {'form': ['do'], 'size': [3], 'tense': ['do_imp.'], 'level': [0.0], 'span': [[[16], [197], [489]]], 'sentence_id': [[0, 2, 2]]}, 'Infinitive passive with "to"': {'form': ['to be done'], 'size': [1], 'tense': ['be done_inf.'], 'level': [2.0], 'span': [[[138, 139, 140]]], 'sentence_id': [[2]]}, 'Infinitive with "to"': {'form': ['to do'], 'size': [19], 'tense': ['do_inf.'], 'level': [0.0], 'span': [[[21, 22], [47, 48], [53, 54], [75, 76], [88, 89], [91, 92], [152, 153], [154, 155], [157, 158], [160, 161], [166, 167], [175, 176], [261, 262], [291, 292], [312, 313], [330, 331], [354, 355], [446, 447], [496, 497]]], 'sentence_id': [[0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]}, 'Infinitive with modal verb: can': {'form': ['can do'], 'size': [3], 'tense': ['do_inf.'], 'level': [0.5], 'span': [[[178, 180], [184, 186], [302, 304]]], 'sentence_id': [[2, 2, 2]]}, 'Infinitive without "to"': {'form': ['do'], 'size': [2], 'tense': ['do_inf.'], 'level': [0.0], 'span': [[[199], [410]]], 'sentence_id': [[2, 2]]}, 'Past simple': {'form': ['did', 'did do', 'was'], 'size': [6, 1, 1], 'tense': ['do_ind. (past)', 'do_ind. (past)', 'do_ind. (past)'], 'level': [0.5, 0.5, 0.5], 'span': [[[95], [100], [171], [300], [353], [375]], [[147, 149]], [[296]]], 'sentence_id': [[2, 2, 2, 2, 2, 2], [2], [2]]}, 'Present continuous': {'form': ['are doing', 'is doing'], 'size': [6, 2], 'tense': ['be doing_ind. (present)', 'be doing_ind. (present)'], 'level': [0.5, 0.5], 'span': [[[19, 20], [257, 259], [274, 276], [387, 389], [436, 437], [506, 508]], [[464, 466], [470, 472]]], 'sentence_id': [[0, 2, 2, 2, 2, 2], [2, 2]]}, 'Present perfect': {'form': ['has done', 'have done'], 'size': [2, 2], 'tense': ['have done_ind. (present)', 'have done_ind. (present)'], 'level': [1.0, 1.0], 'span': [[[105, 106], [105, 109]], [[81, 83], [128, 129]]], 'sentence_id': [[2, 2], [1, 2]]}, 'Present simple': {'form': ['do', 'do do', 'does do', 'is', 'are', 'does', 'have did'], 'size': [11, 9, 5, 5, 4, 2, 1], 'tense': ['do_ind. (present)', 'do_ind. (present)', 'do_ind. (present)', 'do_ind. (present)', 'do_ind. (present)', 'do_ind. (present)', 'do_ind. (present)'], 'level': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'span': [[[5], [36], [42], [52], [59], [87], [220], [225], [281], [294], [450]], [[205, 207], [229, 231], [251, 253], [285, 287], [309, 311], [326, 328], [356, 358], [401, 403], [425, 427]], [[406, 408], [413, 415], [418, 420], [479, 481], [484, 486]], [[7], [25], [337], [349], [474]], [[189], [268], [361], [494]], [[121], [445]], [[128, 135]]], 'sentence_id': [[0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [0, 0, 2, 2, 2], [2, 2, 2, 2], [2, 2], [2]]}, 'Present simple passive': {'form': ['are done', 'is done'], 'size': [1, 1], 'tense': ['be done_ind. (present)', 'be done_ind. (present)'], 'level': [2.0, 2.0], 'span': [[[370, 371]], [[118, 119]]], 'sentence_id': [[2], [2]]}}
        self.clauses = {'advcl': {'clause_form': ['because_0.0', 'how_4.0', 'if_1.0', 'part. (present)_2.0', 'where_4.0'], 'size': [3, 1, 1, 1, 1], 'clause_span': [[[83], [144, 145, 146, 147, 148, 149, 150, 151], [324, 325, 326, 327, 328, 329]], [[183, 184, 185, 186, 190, 191, 192, 193, 194, 195, 196]], [[434, 435, 436, 437, 438, 439, 440, 441, 442, 443]], [[397, 398]], [[187, 188, 189]]], 'sentence_id': [[1, 2, 2], [2], [2], [2], [2]]}, 'cc': {'clause_form': ['and_0.0', 'so_0.0'], 'size': [1, 1], 'clause_span': [[[56, 59]], [[373, 374, 375, 453, 454, 455, 456, 457, 458, 473, 474, 475, 476, 477, 478]]], 'sentence_id': [[1], [2]]}, 'ncl': {'clause_form': ['(that)_2.0', 'how_3.0', 'that_2.0', 'what_3.0', 'what_4.0', 'which_3.0'], 'size': [23, 4, 3, 1, 1, 1], 'clause_span': [[[25, 26, 27, 28, 29, 30, 31, 32], [33, 34, 35, 36, 37, 38, 39, 40], [120, 121, 122], [132, 133, 134, 135, 136, 137], [197], [251, 252, 253, 254, 255, 256], [257, 258, 259], [268, 269, 270, 271, 272, 273], [274, 275, 276, 277, 278], [285, 286, 287, 288, 289, 290], [299, 300], [301, 302, 303, 304, 305, 306, 307], [308, 309, 310, 311, 312, 313, 314, 315], [316, 317, 318, 319, 320, 321, 322, 323], [335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348], [349, 350], [356, 357, 358], [361, 362, 363, 364, 365, 366, 367], [387, 388, 389, 390, 391, 392, 393, 394, 395, 396], [444, 445, 446, 447], [470, 471, 472], [479, 480, 481, 482, 483], [484, 485, 486, 487, 488]], [[177, 178, 179, 180, 181, 182], [204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217], [228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250], [448, 449, 450, 451, 452]], [[85, 88, 89, 90], [123, 124, 125, 126, 127, 128, 129, 130, 131], [491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510]], [[351, 352, 353, 354, 355]], [[17, 18, 19, 20, 21, 22, 23, 24]], [[50, 53, 54, 55]]], 'sentence_id': [[0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2], [1, 2, 2], [2], [0], [1]]}, 'relcl': {'clause_form': ['(that)_1.0', '(that)_2.0', 'how_2.0', 'that_1.0', 'what_2.0'], 'size': [8, 1, 2, 3, 1], 'clause_span': [[[51, 52], [86, 87], [169, 170, 171, 172, 173, 174], [368, 369, 370, 371, 372], [400, 401, 402, 403], [412, 413, 414, 415, 416], [417, 418, 419, 420, 421, 422], [423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433]], [[4, 5, 6]], [[218, 219, 220, 221, 222], [223, 224, 225, 226, 227]], [[99, 100], [279, 280, 281, 282, 283, 284], [405, 406, 407, 408]], [[459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469]]], 'sentence_id': [[1, 1, 2, 2, 2, 2, 2, 2], [0], [2, 2], [2, 2, 2], [2]]}}



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
        if not self.original_transcript:
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

# videoId = '59CmEKAjBzY'
# vid = Video(videoId, 'fr')
# vid.add_video_details()
# vid.add_transcripts()
# print(vid.original_transcript)
# print(vid.translated_transcript)
# vid.add_difficulty()
# print(vid.transcript_text)
# print(vid)
# print(vid.final_levels)
# print(vid.wordlists)
# print(vid.tenses)
# print(vid.clauses)
# print(vid.allowed_remaining)
