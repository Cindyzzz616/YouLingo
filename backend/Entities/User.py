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
    target_language: str  # (if there's time)
    lexicon: dict[str, dict[str, float | int]]  # cefr and frequency are the two keys in the nexted dict
    tenses: dict[str, int]
    clauses: dict[str, int]
    phrases: dict[str, int]

    # TODO make more lexicons for clause type, etc

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

    def add_word_to_lexicon(self, word: str, cefr: float) -> None:
        if word in self.lexicon.keys():
            self.lexicon[word]['freq'] += 1
        else:
            self.lexicon[word] = {'freq': 1, 'cefr': cefr}

    def add_to_tenses(self, tense: str) -> None:
        if tense in self.tenses.keys():
            self.tenses[tense] += 1
        else:
            self.tenses[tense] = 1

    def add_to_clauses(self, clause: str) -> None:
        if clause in self.clauses.keys():
            self.clauses[clause] += 1
        else:
            self.clauses[clause] = 1

    def add_to_phrases(self, phrase: str) -> None:
        if phrase in self.phrases.keys():
            self.phrases[phrase] += 1
        else:
            self.phrases[phrase] = 1
