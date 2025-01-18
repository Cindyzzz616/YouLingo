from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

# Your API key
api_key = 'AIzaSyBT2UKWCmrb9DcK_OLGSegbkd8WDE3-XBI'
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_details(video_id):
    request = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        id=video_id
    )
    response = request.execute()
    return response['items'][0]['snippet']

video_id = 'dQw4w9WgXcQ'  # Replace with your desired video ID
video_details = get_video_details(video_id)
print(video_details)


# Getting the transcript of the video

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        return f"Error: {str(e)}"

video_id = 'dQw4w9WgXcQ'  # Replace with your desired video ID
transcript = get_transcript(video_id)
for entry in transcript:
    print(f"{entry['start']}s: {entry['text']}")
