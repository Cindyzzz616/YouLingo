import pickle

from Video import Video
from User import User

# Initialize the objects and save them to disk - only run after changes are made
video_etymology = Video(path="video_analysis/videos/etymology.MP4",
                        audio_folder="video_analysis/audios")
video_linguistic_intelligence = Video(path="video_analysis/videos/linguistic_intelligence.MP4",
                                      audio_folder="video_analysis/audios")

user = User(net_vocab_size=3000, l1='Mandarin Chinese', word_family_size=1500)

# Create and dump the objects
with open("video_object_etymology.pkl", "wb") as f:
    pickle.dump(video_etymology, f)

with open("video_object_linguistic_intelligence.pkl", "wb") as f:
    pickle.dump(video_linguistic_intelligence, f)

with open("user_object.pkl", "wb") as f:
    pickle.dump(user, f)

# Load the objects from disk
with open("video_object_etymology.pkl", "rb") as f:
    video_etymology = pickle.load(f)

with open("video_object_linguistic_intelligence.pkl", "rb") as f:
    video_linguistic_intelligence = pickle.load(f)

with open("user_object.pkl", "rb") as f:
    user = pickle.load(f)