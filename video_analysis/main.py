import User
import Video

import lexical_profile
import lexical_coverage

def analyze_video_difficulty(video: Video, user: User):


    # lexical factors
    lexical_profile = lexical_profile(transcript)
    lexical_coverage = lexical_coverage(transcript, user)

    # phonetic factors
    speech_rate = speech_rate(video, transcript)

    # calculate difficulty score
    difficulty_score = 0.0

    return difficulty_score

def rank_videos(videos: list, user: User):
    pass

if __name__ == "__main__":
    # initialize a user with a given vocabulary size
    VOCAB_SIZE = 3000
    user = User.User(VOCAB_SIZE)
    print(f"User Lexicon: {user.lexicon}")

    # process a single video
    video = Video.Video(path="video_analysis/linguistic_intelligence.MP4")
    print(video)
    video1 = Video.Video(path="video_analysis/etymology.MP4")
    print(video1)

    # lexical coverage
    print(f"Lexical coverage: {lexical_coverage.lexical_coverage(video, user)}")
    print(f"Lexical coverage: {lexical_coverage.lexical_coverage(video1, user)}")

    # overall difficulty (to be implemented)
    difficulty_score = analyze_video_difficulty(video, user)
    print(f"Video Difficulty Score: {difficulty_score}")

    # rank multiple videos
    video_paths = ["video_analysis/video1.MP4", "video_analysis/video2.MP4"]
    for path in video_paths:
        video = Video(path=path)
        difficulty_score = analyze_video_difficulty(video, user)
        print(f"Video: {path}, Difficulty Score: {difficulty_score}")
    ranking = rank_videos(video_paths, user)
    print(f"Video Rankings: {ranking}")

