# NOTE in general, I need some function or module that takes in data from both a video and a user

from User import User
from Video import Video

import test_objects

from lexical_coverage import lexical_coverage
from phonetic_coverage import phonetic_coverage_by_phonemes, phonetic_coverage_by_words
from adjust_speech_rate import adjust_speech_rate
from translate import translate_text

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

if __name__ == "__main__":
    video = test_objects.video_etymology
    user = test_objects.user
    # adjusting speech rate
    # target_rate = 150  # example target rate
    # target_type = 'wpm'  # example target type
    # adjust_speech_rate(video, target_rate, target_type)
    
    # target_rate = 200
    # target_type = 'spm'
    # adjust_speech_rate(video, target_rate, target_type)

    # target_rate = 0.8
    # target_type = 'factor'
    # adjust_speech_rate(video, target_rate, target_type)

    # target_rate = 100
    # target_type = 'duration'
    # adjust_speech_rate(video, target_rate, target_type)

    # translating transcripts
    translation = translate_text(video.transcript_text, to_code=user.l1)
    print(f"Translated Transcript: {translation}")

    # overall difficulty (to be implemented)
    difficulty_score = analyze_video_difficulty(video, user)
    print(f"Video Difficulty Score: {difficulty_score}")

    # rank multiple videos
    # video_paths = ["video_analysis/video1.MP4", "video_analysis/video2.MP4"]
    # for path in video_paths:
    #     video = Video(path=path)
    #     difficulty_score = analyze_video_difficulty(video, user)
    #     print(f"Video: {path}, Difficulty Score: {difficulty_score}")
    # ranking = rank_videos(video_paths, user)
    # print(f"Video Rankings: {ranking}")

