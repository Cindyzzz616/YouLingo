# instantiate the pipeline
from pyannote.audio import Pipeline
import os

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

def diarize(audio_path: str):
    """
    Return the number of speakers found in a video. Also write a rttm file with results.
    """
    pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=HF_TOKEN)

    # run the pipeline on an audio file
    diarization = pipeline(audio_path)

    # dump the diarization output to disk using RTTM format
    rttm_file_name = audio_path.replace('.wav', '')
    with open(f"{rttm_file_name}.rttm", "w") as rttm:
        diarization.write_rttm(rttm)

    speakers = set()

    with open(f"{rttm_file_name}.rttm", "r") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split()
            if parts[0] == "SPEAKER":
                speakers.add(parts[7])  # 8th column is speaker label

    # print("Speakers found:", speakers)
    # print("Number of speakers:", len(speakers))

    return len(speakers)
