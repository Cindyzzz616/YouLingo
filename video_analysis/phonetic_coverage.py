from Video import Video
from User import User

def phonetic_coverage(video: Video, user: User):
    """
    Calculate the phonetic coverage of a video for a given user.
    * mark the words in the transcript that are not in the user's phonetic inventory
    ** return that as a list? Or a dictionary?
    *** with keys as words and values as dictionaries with keys "phonemes", "known phonemes", "unknown phonemes"
    * highlight the specific phonemes
    * compute a coverage score: number of words with no unknown phonemes / total words in transcript
    * compute a different coverage score: number of known phonemes / total phonemes in transcript
    NOTE still need to answer the token vs type question
    """
    coverage = 0.0
    return coverage