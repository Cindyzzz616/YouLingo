"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect

@dataclass
class AudioLoop(Effect):
    """Loops over an audio clip.

    Returns an audio clip that plays the given clip either
    `n_loops` times, or during `duration` seconds.

    Examples
    --------

    .. code:: python

        from moviepy import *
        videoclip = VideoFileClip('myvideo.mp4')
        music = AudioFileClip('music.ogg')
        audio = music.with_effects([afx.AudioLoop(duration=videoclip.duration)])
        videoclip.with_audio(audio)

    """
    n_loops: int = ...
    duration: float = ...
    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        ...
    


