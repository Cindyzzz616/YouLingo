# NOTE do we want to aim for a specific phonation time ratio?

from moviepy import VideoFileClip, concatenate_videoclips, vfx

from Video import Video
from test_objects import video_etymology

def insert_pauses(video: Video, adjustment_factor: float):
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

if __name__ == "__main__":
    insert_pauses(video_etymology, 0.5)