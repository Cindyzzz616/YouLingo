import pickle

from Video import Video
from User import User

# Initialize the objects and save them to disk - only run after changes are made
# video_etymology = Video(path="video_analysis/videos/etymology.MP4")
# video_linguistic_intelligence = Video(path="video_analysis/videos/linguistic_intelligence.MP4")

# user = User(vocab_size=3000, l1='Mandarin Chinese')


# with open("video_object_etymology.pkl", "wb") as f:
#     pickle.dump(video_etymology, f)

# with open("video_object_linguistic_intelligence.pkl", "wb") as f:
#     pickle.dump(video_linguistic_intelligence, f)

# with open("user_object.pkl", "wb") as f:
#     pickle.dump(user, f)

# Load the objects from disk
with open("video_object_etymology.pkl", "rb") as f:
    video_etymology = pickle.load(f)

with open("video_object_linguistic_intelligence.pkl", "rb") as f:
    video_linguistic_intelligence = pickle.load(f)

with open("user_object.pkl", "rb") as f:
    user = pickle.load(f)