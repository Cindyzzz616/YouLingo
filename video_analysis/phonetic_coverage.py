from Video import Video
from User import User
import test_objects

def get_marked_word_list(video: Video, user: User):
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
    marked_word_list = {}
    i = 0
    for phonemes_of_word in video.phoneme_list:
        word = video.word_list[i]
        marked_word_list[word] = {
            'phonemes': phonemes_of_word,
            'known_phonemes': [],
            'unknown_phonemes': []
        }
        for phoneme in phonemes_of_word:
            if phoneme not in user.phonetic_inventory:
                # This phoneme is not in the user's inventory
                # Mark it as unknown
                marked_word_list[word]['unknown_phonemes'].append(phoneme)
            else:
                # This phoneme is known to the user
                marked_word_list[word]['known_phonemes'].append(phoneme)
        i += 1
    return marked_word_list

def get_words_with_unknown_phonemes(marked_word_list: dict):
    """
    Get a list of words that have unknown phonemes.
    """
    words_with_unknown_phonemes = {}
    for word in marked_word_list.keys():
        if marked_word_list[word]['unknown_phonemes']:
            words_with_unknown_phonemes[word] = marked_word_list[word]
    return words_with_unknown_phonemes

def phonetic_coverage_by_words(marked_word_list: dict, words_with_unknown_phonemes: dict):
    """
    Compute the phonetic coverage scores based on the words in the marked word list.
    """
    unknown_percentage = len(words_with_unknown_phonemes) / len(marked_word_list) if len(marked_word_list) > 0 else 0
    return 1 - unknown_percentage

def phonetic_coverage_by_phonemes(marked_word_list: dict, user: User):
    """
    Compute the phonetic coverage scores based on the total phonemes in the marked word list.
    """
    total_phonemes = []
    known_phonemes = []
    for word in marked_word_list.keys():
        total_phonemes.extend(marked_word_list[word]['phonemes'])
        known_phonemes.extend(marked_word_list[word]['known_phonemes'])

    # this is calculating by tokens, not types
    # if we want to calculate by types, we can use set() to get unique phonemes
    # total_phonemes = set(total_phonemes)
    # known_phonemes = set(known_phonemes)
    coverage = len(known_phonemes) / len(total_phonemes) if len(total_phonemes) > 0 else 0
    return coverage

if __name__ == "__main__":
    # Example usage

    # Initialize a user with a given vocabulary size and first language
    # VOCAB_SIZE = 3000
    # L1 = 'Nepali'
    # user = User(VOCAB_SIZE, L1)
    # print(f"User's phonetic inventory: {user.phonetic_inventory}")

    # Initialize a video object
    # video = Video(path="video_analysis/videos/etymology.MP4")
    # print(video)

    video = test_objects.video_linguistic_intelligence
    user = test_objects.user

    marked_word_list = get_marked_word_list(video, user)
    print(f"Marked Word List: {marked_word_list}\n")

    words_with_unknown_phonemes = get_words_with_unknown_phonemes(marked_word_list)
    print(f"Words with unknown phonemes: {words_with_unknown_phonemes}")

    word_coverage_score = phonetic_coverage_by_words(marked_word_list, words_with_unknown_phonemes)
    print(f"Word Coverage Score: {word_coverage_score:.3f}")

    phoneme_coverage_score = phonetic_coverage_by_phonemes(marked_word_list, user)
    print(f"Phoneme Coverage Score: {phoneme_coverage_score:.3f}")
