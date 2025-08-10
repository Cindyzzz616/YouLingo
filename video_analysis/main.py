# NOTE in general, I need some function or module that takes in data from both a video and a user

from User import User
from Video import Video

import test_objects

from lexical_coverage import lexical_coverage
from phonetic_coverage import phonetic_coverage_by_phonemes, phonetic_coverage_by_words
from adjust_speech_rate import adjust_speech_rate
from translate import translate_text

### An example of the simplest formula for difficulty score: a rating for each factor (out of 100 perhaps?), 
# multiplied by coefficients that represent the factor's weight. So we also need to find a way to convert each
# raw measurement into a percentage rating. But the main objective of the new study is basically to find the
# coefficients (or fit a new formula to the actual data on the independent vs dependent variable graph)
# NOTE: not sure if the difficulty score needs to be relative to a user or an absolute score (relative to the
# language as a whole?)

# Coefficients to weigh the factors in the difficulty score
LEXICAL_WEIGHT = 0.4
PHONETIC_WEIGHT = 0.3

def analyze_video_difficulty(video: Video, user: User):
    # lexical factors
    lex_cov_raw = lexical_coverage(video, user)[0]
    lex_cov_inferencing = lexical_coverage(video, user)[1]

    # phonetic factors
    phon_cov_phonemes = phonetic_coverage_by_phonemes(video, user)
    phon_cov_words = phonetic_coverage_by_words(video, user)

    # calculate difficulty score
    difficulty_score = (LEXICAL_WEIGHT * lex_cov_raw) + (PHONETIC_WEIGHT * phon_cov_phonemes)

    return difficulty_score

### the driver for the entire video analysis algorithm ###

if __name__ == "__main__":
    video = test_objects.video_etymology
    user = test_objects.user

    # Displaying video and user data
    print(video)
    print(user)

    # Modifying videos and saving them as new files
    # adjust speech rate
    # translation


    # Translating transcripts
    translation = translate_text(video.transcript_text, to_lang=user.l1)
    print(f"Translated Transcript: {translation}")

    # Displaying difficulty score (to be implemented)

    difficulty_score = analyze_video_difficulty(video, user)
    print(f"Video Difficulty Score: {difficulty_score}")

    # Ranking multiple videos
    # video_paths = ["video_analysis/video1.MP4", "video_analysis/video2.MP4"]
    # for path in video_paths:
    #     video = Video(path=path)
    #     difficulty_score = analyze_video_difficulty(video, user)
    #     print(f"Video: {path}, Difficulty Score: {difficulty_score}")
    # ranking = rank_videos(video_paths, user)
    # print(f"Video Rankings: {ranking}")

