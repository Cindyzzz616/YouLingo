"""
This type stub file was generated by pyright.
"""

"""
On the long term this will implement several methods to make videos
out of VideoClips
"""
class FFMPEG_VideoWriter:
    """A class for FFMPEG-based video writing.

    Parameters
    ----------

    filename : str
      Any filename like ``"video.mp4"`` etc. but if you want to avoid
      complications it is recommended to use the generic extension ``".avi"``
      for all your videos.

    size : tuple or list
      Size of the output video in pixels (width, height).

    fps : int
      Frames per second in the output video file.

    codec : str, optional
      FFMPEG codec. It seems that in terms of quality the hierarchy is
      'rawvideo' = 'png' > 'mpeg4' > 'libx264'
      'png' manages the same lossless quality as 'rawvideo' but yields
      smaller files. Type ``ffmpeg -codecs`` in a terminal to get a list
      of accepted codecs.

      Note for default 'libx264': by default the pixel format yuv420p
      is used. If the video dimensions are not both even (e.g. 720x405)
      another pixel format is used, and this can cause problem in some
      video readers.

    audiofile : str, optional
      The name of an audio file that will be incorporated to the video.

    audio_codec : str, optional
      FFMPEG audio codec. If None, ``"copy"`` codec is used.

    preset : str, optional
      Sets the time that FFMPEG will take to compress the video. The slower,
      the better the compression rate. Possibilities are: ``"ultrafast"``,
      ``"superfast"``, ``"veryfast"``, ``"faster"``, ``"fast"``,  ``"medium"``
      (default), ``"slow"``, ``"slower"``, ``"veryslow"``, ``"placebo"``.

    bitrate : str, optional
      Only relevant for codecs which accept a bitrate. "5000k" offers
      nice results in general.

    with_mask : bool, optional
      Set to ``True`` if there is a mask in the video to be encoded.

    pixel_format : str, optional
      Optional: Pixel format for the output video file. If is not specified
      ``"rgb24"`` will be used as the default format unless ``with_mask`` is
      set as ``True``, then ``"rgba"`` will be used.

    logfile : int, optional
      File descriptor for logging output. If not defined, ``subprocess.PIPE``
      will be used. Defined using another value, the log level of the ffmpeg
      command will be "info", otherwise "error".

    threads : int, optional
      Number of threads used to write the output with ffmpeg.

    ffmpeg_params : list, optional
      Additional parameters passed to ffmpeg command.
    """
    def __init__(self, filename, size, fps, codec=..., audiofile=..., audio_codec=..., preset=..., bitrate=..., with_mask=..., logfile=..., threads=..., ffmpeg_params=..., pixel_format=...) -> None:
        ...
    
    def write_frame(self, img_array): # -> None:
        """Writes one frame in the file."""
        ...
    
    def close(self): # -> None:
        """Closes the writer, terminating the subprocess if is still alive."""
        ...
    
    def __enter__(self): # -> Self:
        ...
    
    def __exit__(self, exc_type, exc_value, traceback): # -> None:
        ...
    


def ffmpeg_write_video(clip, filename, fps, codec=..., bitrate=..., preset=..., write_logfile=..., audiofile=..., audio_codec=..., threads=..., ffmpeg_params=..., logger=..., pixel_format=...): # -> None:
    """Write the clip to a videofile. See VideoClip.write_videofile for details
    on the parameters.
    """
    ...

def ffmpeg_write_image(filename, image, logfile=..., pixel_format=...): # -> None:
    """Writes an image (HxWx3 or HxWx4 numpy array) to a file, using ffmpeg.

    Parameters
    ----------

    filename : str
        Path to the output file.

    image : np.ndarray
        Numpy array with the image data.

    logfile : bool, optional
        Writes the ffmpeg output inside a logging file (``True``) or not
        (``False``).

    pixel_format : str, optional
        Pixel format for ffmpeg. If not defined, it will be discovered checking
        if the image data contains an alpha channel (``"rgba"``) or not
        (``"rgb24"``).
    """
    ...

