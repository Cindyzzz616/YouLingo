from pathlib import Path

folder = Path("video_analysis/sampled_videos")

i = 1

for file in folder.iterdir():
    if file.is_file():
        new_name = f"{i}_video.mp4"  # Change this pattern
        file.rename(folder / new_name)
        i += 1
