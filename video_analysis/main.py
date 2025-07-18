import User
import Video
import transcript
import audio
import lexical_profile
import lexical_coverage
import speech_rate

def analyze_video_difficulty(video: Video, user: User):
    # preprocess the video
    transcript = transcript(video)
    audio = audio(video)

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
    # process a single video
    video = Video(path="etymology.MP4")
    user = User()
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

