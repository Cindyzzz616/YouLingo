import Video
import whisper

def transcribe(video: Video):
    model = whisper.load_model("base")  # or "small", "medium", "large"
    result = model.transcribe(video.path)
    return result['text']

# Example
video = Video.Video("video_analysis/etymology.MP4")
transcript = transcribe(video)
print(transcript)