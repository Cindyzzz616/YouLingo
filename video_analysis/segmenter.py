from inaSpeechSegmenter import Segmenter
from pydub import AudioSegment

import numpy as np

# # 1) Restore numpy.lib.pad for older libs expecting it
# if not hasattr(np.lib, "pad"):
#     np.lib.pad = np.pad  # map to the correct function

# # 2) Patch pyannote viterbi to not pass a generator to np.vstack (NumPy 2.x disallows it)
# try:
#     from pyannote.algorithms.utils import viterbi as _viterbi
#     def _patched_update_emission(emission, consecutive):
#         # original used a generator; wrap in list for NumPy 2.x
#         return np.vstack([emission[i::consecutive] for i in range(consecutive)])
#     _viterbi._update_emission = _patched_update_emission
# except Exception:
#     pass  # if pyannote isn't present yet or structure differs, ignore

# # swap it in
# _viterbi._update_emission = _patched_update_emission

def percent_speech_music(wav_path):
    seg = Segmenter(vad_engine='smn', detect_gender=False)  # smn = speech/music/noise
    timeline = seg(wav_path)  # list of tuples: (label, start, end)

    dur = AudioSegment.from_wav(wav_path).duration_seconds
    speech = sum(e-s for lab, s, e in timeline if lab == 'speech')
    music  = sum(e-s for lab, s, e in timeline if lab == 'music')
    return {
        "duration": dur,
        "speech_seconds": speech,
        "music_seconds": music,
        "speech_pct": speech/dur if dur else 0.0,
        "music_pct": music/dur if dur else 0.0,
        "segments": timeline,
    }

result = percent_speech_music("/Users/cindyzhang/YouLingo/video_analysis/audios/etymology_audio.wav")
print(result)