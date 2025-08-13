import nltk
nltk.download('punkt')  # only need to run once

from nltk.tokenize import sent_tokenize

# Example transcript from Whisper
text = "Where do you put your belt during squats and deadlifts because I'm getting some bruising?  Well, keep in mind I actually use two different belts. I use an SPD belt for my squats  because it is a heftier belt and I prefer setting it a little bit lower.  For some reason it's easier on my hip that way and also keep in mind I've got a short  a short torso than most people but that's about where I like to set it during squats.  Sassy belt flake. For deadlifts I use my A7 belt because it is a little bit of a  looser belt and I prefer setting it higher actually because it allows me to  get into a much better position that way and also I like having this looser for deadlifts  than I do for squats again just because it allows me to get to a better position.  So yeah, that's why I set my belts."

# Split into sentences
sentences = sent_tokenize(text)

for sentence in sentences:
    print(sentence, "\n")
# Output:
# ['This is the first sentence.', "Here's another one!", 'And a third sentence?']