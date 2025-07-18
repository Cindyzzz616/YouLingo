from moviepy.editor import VideoFileClip

def extract_audio_moviepy(video_path: str, audio_path: str):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

# Example usage
video_path = "video_analysis/etymology.MP4"
audio_path = "video_analysis/etymology_audio.wav"
extract_audio_moviepy(video_path, audio_path)