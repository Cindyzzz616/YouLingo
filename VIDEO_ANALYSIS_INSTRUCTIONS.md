# Video analysis instructions

## File structure

There are three types of objects: Video, User and Word.
test_object contains pickled Video and User objects.

Folders:

- audios: audios extracted from individual videos
- videos: individual videos
- sampled_videos: 1000 trending tiktok videos from 2021
- sampled_audios: audios extracted from sampled videos

## Video attributes

- Transcript (native Whisper format and full text)
- Length (duration in seconds)
- Speech length (duration of speech)
- Tokens (a list of Word objects that represents the tokens in the video)
- Types (a list of Word objects that represents the types/unique words in the video)
- Word count
- Words per minute (wpm) - calculated based on speech duration
- Syllables per minute (spm)
- Average PTR

## User attributes

- Vocabulary size
- Lexicon (based on frequency lists + vocabulary size for now)
- Native language (L1)
- Phonetic inventory (sounds they know from native language)

## User + video attributes
- Lexical coverage
- Phonetic coverage

## Modification features

- google_translate and translate: Translate the text of a transcript into a user's native language
- insert_pauses: Insert pauses of specified durations between sentences
- adjust_speech_rate: Adjust the speed of a video to a specified wpm, spm, duration or by a specified factor

## TODOs

- [x] fix language_code
- [ ] when recognizing transcripts, add something to check whether the video has speech and what language the speech is in... or basically detect all the properties in my tiktok resampling table
- [ ] fix calculate ptr stuff in Video
- [ ] get better corpus for word frequency (or just deal with contractions and apostrophes in general, and count by word families not words)
- [ ] add speaker diarization to get number of speakers in a video
- [ ] fix pitch issue after adjusting speed
- [x] phonological neighbours
- [x] FL (NOTE: we can also see how often a specific user confuses two phonemes in transcription exercises - and make a confusion matrix based on that; can also combine FL and phonetic overlap - if a word has a sound with high FL, but that sound/distinction is in the user's L1 inventory, then it's probably less likely to be confused than otherwise)

## Metrics to potentially add

- type-token ratio of a video
- average syllable count of words in a video (syllable/word)
- count word frequency by word *families*
