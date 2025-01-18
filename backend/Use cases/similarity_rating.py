from backend.Entities import User, Video

class SimilarityRating:
    """
    Compares the words, tenses and clauses in the transcript of a video and the
    knowledge base of a user.
    """

    video: Video
    user: User

    def __init__(self, video: Video, user: User):
        self.video = video
        self.user = user

    def word_similarity(self) -> float:
        """
        Returns the similarity percentage between the words in the video and the
        words in the user's lexicon.
        """
        # if there's time - also return the list of matched words for highlighting
        total_transcript_words = 0
        matched_words = []
        for cefr_level in self.video.wordlists.keys():
            for word in self.video.wordlists[cefr_level]['lemma']:
                if word in self.user.lexicon.keys():
                    self.user.lexicon[word]['freq'] += 1
                    matched_words.append(word)
                else:
                    self.user.lexicon[word] = {'freq': 1, 'cefr': cefr_level}
                total_transcript_words += 1
        return len(matched_words) / total_transcript_words

    def tense_similarity(self) -> float:
        total_transcript_tenses = len(self.video.tenses)
        matched_tenses = []
        for tense in self.video.tenses.keys():
            if tense in self.user.tenses.keys():
                self.user.tenses[tense] += 1
                matched_tenses.append(tense)
            else:
                self.user.tenses[tense] = 1
        return len(matched_tenses) / total_transcript_tenses

    def clause_similarity(self) -> float:
        total_transcript_clauses = len(self.video.clauses)
        matched_clauses = []
        for clause in self.video.clauses.keys():
            if clause in self.user.clauses.keys():
                self.user.clauses[clause] += 1
                matched_clauses.append(clause)
            else:
                self.user.tenses[clause] = 1
        return len(matched_clauses) / total_transcript_clauses

    def overall_similarity(self) -> float:
        return (self.word_similarity() + self.tense_similarity() +
                self.clause_similarity()) / 3
