from moviepy import VideoFileClip, vfx

from Video import Video
from test_objects import video_etymology

def adjust_speech_rate(video: Video, target: float, target_type: str):
    """
    Adjust the speech rate of the video by changing the playback speed. Saves the adjusted video as a new file.
    
    :param video: An instance of Video containing the video file.
    :param target: The desired speech rate.
    :param target_type: The unit of measurement. It can be 'wpm' (words per minute), 'spm' (syllables per minute), 'factor' (multiplicative factor), or 'duration' (target duration in seconds).
    :return: None
    """
    if target <= 0:
        raise ValueError("Target must be a positive number.")
    
    # Load your video
    clip = VideoFileClip(video.path)
    
    # Adjust the playback speed based on the specified rate type
    if target_type == 'wpm':
        adjustment_factor = target / video.wpm
    elif target_type == 'spm':
        adjustment_factor = target / video.spm
    elif target_type == 'factor':
        adjustment_factor = target
    elif target_type == 'duration':
        adjustment_factor = target / video.length
    else:
        raise ValueError("Invalid rate type. Use 'wpm', 'spm', or 'factor'.")

    adjusted_clip = clip.with_effects([vfx.MultiplySpeed(adjustment_factor)])

    output_path = 'video_analysis/videos/' + video.path.split('/')[-1].replace(
        ".MP4", f"_adjusted_{target}_{target_type}.MP4"
    )

    adjusted_clip.write_videofile(output_path)

if __name__ == '__main__':
    video = video_etymology
    
    target_rate = 150  # example target rate
    target_type = 'wpm'  # example target type
    adjust_speech_rate(video, target_rate, target_type)
    
    target_rate = 200
    target_type = 'spm'
    adjust_speech_rate(video, target_rate, target_type)

    target_rate = 0.8
    target_type = 'factor'
    adjust_speech_rate(video, target_rate, target_type)

    target_rate = 100
    target_type = 'duration'
    adjust_speech_rate(video, target_rate, target_type)