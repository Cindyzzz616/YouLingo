# NOTE do we want to aim for a specific phonation time ratio?
# NOTE current issue - it's hard to take the pause between sentences or words and slow down the pause itself, for a smoother transition - it's only possible to freeze the frame for now

from moviepy import VideoFileClip, concatenate_videoclips, vfx, video
from moviepy.video.fx.Freeze import Freeze
2
from Video import Video
from test_objects import video_etymology
from VAT import preprocess_audio
from faster_whisper import WhisperModel
import string

def insert_pauses(video: Video, adjustment_factor: float):
    """A test function that inserts pauses at a specific point in time."""
    # Load full video
    clip = VideoFileClip(video.path)

    # Define segments
    segment1 = clip.subclipped(0, 5)                 # Normal speed (0–5s)
    segment2 = clip.subclipped(5, 10).with_effects([vfx.MultiplySpeed(adjustment_factor)])  # Slow down (5–10s) to half speed
    segment3 = clip.subclipped(10, clip.duration)   # Normal speed again

    # Concatenate segments
    final = concatenate_videoclips([segment1, segment2, segment3])

    # Export final video
    output_path = 'video_analysis/videos/' + video.path.split('/')[-1].replace(
        ".MP4", f"_pauses_inserted_{adjustment_factor}.MP4"
    )
    final.write_videofile(output_path)
    print(output_path)

def insert_pauses_between_sentences(video: Video, pause_duration: float):
    clip = VideoFileClip(video.path)
    total_freeze_duration = 0

    for segment in video.transcript['segments']:
        print(segment.start)
        print(segment.text)
        print(segment.end)

        # Create a freeze effect
        freeze_effect = Freeze(t=segment.end + total_freeze_duration, freeze_duration=pause_duration).copy()

        # Apply the effect to your clip
        clip = freeze_effect.apply(clip)

        # increment the total freeze duration
        total_freeze_duration += pause_duration
    
    
    # Export final video
    output_path = 'video_analysis/videos/' + video.path.split('/')[-1].replace(
        ".MP4", f"_pauses_inserted_between_sentences_{pause_duration}_seconds.MP4"
    )
    clip.write_videofile(output_path)
    print(output_path)

def insert_pauses_at_punctuations(video: Video, pause_duration: float):

    processed_path = preprocess_audio(video.audio_path)
    model = WhisperModel("base", compute_type="int8")  # or "medium", "large"
    segments, _ = model.transcribe(processed_path, word_timestamps=True)

    clip = VideoFileClip(video.path)
    total_freeze_duration = 0

    for segment in segments:
        if segment.words is not None:
            for word in segment.words:
                if word.word[-1] in string.punctuation:
                    print(word)

                    #  Create a freeze effect
                    freeze_effect = Freeze(t=word.end + total_freeze_duration, freeze_duration=pause_duration).copy()

                    # Apply the effect to your clip
                    clip = freeze_effect.apply(clip)

                    # increment the total freeze duration
                    total_freeze_duration += pause_duration
    
    # Export final video
    output_path = 'video_analysis/videos/' + video.path.split('/')[-1].replace(
        ".MP4", f"_pauses_inserted_at_punctuations_{pause_duration}_seconds.MP4"
    )
    clip.write_videofile(output_path)
    print(output_path)

if __name__ == "__main__":
    # insert_pauses(video_etymology, 0.5)
    # insert_pauses_at_punctuations(video_etymology, 2)
    insert_pauses_between_sentences(video_etymology, 2)