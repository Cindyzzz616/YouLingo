import webrtcvad
import collections
from pydub import AudioSegment
import contextlib
import wave
from faster_whisper import WhisperModel

from pydub import AudioSegment

def preprocess_audio(path):
    audio = AudioSegment.from_file(path)
    audio = audio.set_channels(1)       # mono
    audio = audio.set_frame_rate(16000) # 16kHz
    audio = audio.set_sample_width(2)   # 16-bit PCM
    output_path = "temp.wav"
    audio.export(output_path, format="wav")
    return output_path

def wav_from_video(video_path, wav_path="temp.wav"):
    # Use ffmpeg to extract audio
    import subprocess
    subprocess.run(["ffmpeg", "-y", "-i", video_path, "-ar", "16000", "-ac", "1", wav_path])

def get_voiced_intervals(wav_path, aggressiveness=2, frame_duration_ms=30):
    vad = webrtcvad.Vad(aggressiveness)
    audio = AudioSegment.from_wav(wav_path)
    samples = audio.raw_data
    sample_rate = audio.frame_rate
    frame_size = int(sample_rate * frame_duration_ms / 1000)
    voiced_intervals = []
    is_voiced = False
    start = 0
    for i in range(0, len(samples), frame_size * 2):  # 2 bytes per sample
        frame = samples[i:i + frame_size * 2]
        if len(frame) < frame_size * 2:
            break
        if vad.is_speech(frame, sample_rate):
            if not is_voiced:
                start = i / (sample_rate * 2)
                is_voiced = True
        else:
            if is_voiced:
                end = i / (sample_rate * 2)
                voiced_intervals.append((start, end))
                is_voiced = False
    if is_voiced:
        voiced_intervals.append((start, len(samples) / (sample_rate * 2)))
    return voiced_intervals

def compute_ptrs(segments, voiced_intervals):
    ptrs = []
    ptrs_list = []
    for seg in segments:
        start, end = seg.start, seg.end
        duration = end - start
        speech_time = sum(
            max(0, min(v_end, end) - max(v_start, start))
            for v_start, v_end in voiced_intervals
            if v_end > start and v_start < end
        )
        ptr = speech_time / duration if duration > 0 else 0
        ptrs_list.append(ptr)
        ptrs.append({
            "text": seg.text,
            "start": start,
            "end": end,
            "ptr": round(ptr, 3)
        })
    return ptrs, (sum(ptrs_list) / len(ptrs_list) if ptrs_list else 0)

def compute_ptrs_from_audio(audio_path):
    """
    Compute PTR (Phonation Time Ratio) from an audio file.
    """
    processed_path = preprocess_audio(audio_path)
    voiced_intervals = get_voiced_intervals(processed_path)
    model = WhisperModel("base", compute_type="int8")  # or "medium", "large"
    segments, _ = model.transcribe(processed_path, word_timestamps=True)
    ptrs, average_ptr = compute_ptrs(segments, voiced_intervals)
    # print(segments)
    # print(ptrs)
    print(f"Average PTR: {average_ptr:.3f}")
    return average_ptr