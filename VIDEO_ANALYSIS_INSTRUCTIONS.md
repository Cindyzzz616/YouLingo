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

- [ ] fix language_code
- [ ] fix calculate ptr stuff in Video
- [ ] get better corpus for word frequency (or just deal with contractions and apostrophes in general, and count by word families not words)
- [ ] add speaker diarization to get number of speakers in a video
- [ ] fix pitch issue after adjusting speed
- [x] phonological neighbours
- [ ] FL

## Metrics to potentially add

- type-token ratio of a video
- average syllable count of words in a video (syllable/word)
- count word frequency by word *families*
