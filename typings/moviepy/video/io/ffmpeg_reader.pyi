"""
This type stub file was generated by pyright.
"""

"""Implements all the functions to read a video or a picture using ffmpeg."""
class FFMPEG_VideoReader:
    """Class for video byte-level reading with ffmpeg."""
    def __init__(self, filename, decode_file=..., print_infos=..., bufsize=..., pixel_format=..., check_duration=..., target_resolution=..., resize_algo=..., fps_source=...) -> None:
        ...
    
    def initialize(self, start_time=...): # -> None:
        """
        Opens the file, creates the pipe.

        Sets self.pos to the appropriate value (1 if start_time == 0 because
        it pre-reads the first frame).
        """
        ...
    
    def skip_frames(self, n=...): # -> None:
        """Reads and throws away n frames"""
        ...
    
    def read_frame(self):
        """
        Reads the next frame from the file.
        Note that upon (re)initialization, the first frame will already have been read
        and stored in ``self.last_read``.
        """
        ...
    
    def get_frame(self, t):
        """Read a file video frame at time t.

        Note for coders: getting an arbitrary frame in the video with
        ffmpeg can be painfully slow if some decoding has to be done.
        This function tries to avoid fetching arbitrary frames
        whenever possible, by moving between adjacent frames.
        """
        ...
    
    @property
    def lastread(self):
        """Alias of `self.last_read` for backwards compatibility with MoviePy 1.x."""
        ...
    
    def get_frame_number(self, t): # -> int:
        """Helper method to return the frame number at time ``t``"""
        ...
    
    def close(self, delete_lastread=...): # -> None:
        """Closes the reader terminating the process, if is still open."""
        ...
    
    def __del__(self): # -> None:
        ...
    


def ffmpeg_read_image(filename, with_mask=..., pixel_format=...):
    """Read an image file (PNG, BMP, JPEG...).

    Wraps FFMPEG_Videoreader to read just one image.
    Returns an ImageClip.

    This function is not meant to be used directly in MoviePy.
    Use ImageClip instead to make clips out of image files.

    Parameters
    ----------

    filename
      Name of the image file. Can be of any format supported by ffmpeg.

    with_mask
      If the image has a transparency layer, ``with_mask=true`` will save
      this layer as the mask of the returned ImageClip

    pixel_format
      Optional: Pixel format for the image to read. If is not specified
      'rgb24' will be used as the default format unless ``with_mask`` is set
      as ``True``, then 'rgba' will be used.

    """
    ...

class FFmpegInfosParser:
    """Finite state ffmpeg `-i` command option file information parser.
    Is designed to parse the output fast, in one loop. Iterates line by
    line of the `ffmpeg -i <filename> [-f null -]` command output changing
    the internal state of the parser.

    Parameters
    ----------

    filename
      Name of the file parsed, only used to raise accurate error messages.

    infos
      Information returned by FFmpeg.

    fps_source
      Indicates what source data will be preferably used to retrieve fps data.

    check_duration
      Enable or disable the parsing of the duration of the file. Useful to
      skip the duration check, for example, for images.

    decode_file
      Indicates if the whole file has been decoded. The duration parsing strategy
      will differ depending on this argument.
    """
    def __init__(self, infos, filename, fps_source=..., check_duration=..., decode_file=...) -> None:
        ...
    
    def parse(self): # -> dict[str, Any]:
        """Parses the information returned by FFmpeg in stderr executing their binary
        for a file with ``-i`` option and returns a dictionary with all data needed
        by MoviePy.
        """
        ...
    
    def parse_data_by_stream_type(self, stream_type, line):
        """Parses data from "Stream ... {stream_type}" line."""
        ...
    
    def parse_audio_stream_data(self, line): # -> dict[Any, Any]:
        """Parses data from "Stream ... Audio" line."""
        ...
    
    def parse_video_stream_data(self, line): # -> dict[Any, Any]:
        """Parses data from "Stream ... Video" line."""
        ...
    
    def parse_fps(self, line): # -> float:
        """Parses number of FPS from a line of the ``ffmpeg -i`` command output."""
        ...
    
    def parse_tbr(self, line): # -> float:
        """Parses number of TBS from a line of the ``ffmpeg -i`` command output."""
        ...
    
    def parse_duration(self, line): # -> Any | float | Literal[0]:
        """Parse the duration from the line that outputs the duration of
        the container.
        """
        ...
    
    def parse_metadata_field_value(self, line): # -> tuple[Any, Any] | tuple[Literal[''], Literal['']]:
        """Returns a tuple with a metadata field-value pair given a ffmpeg `-i`
        command output line.
        """
        ...
    
    def video_metadata_type_casting(self, field, value): # -> tuple[Literal['rotate'], float] | tuple[Literal['displaymatrix'], float] | tuple[Any | Literal['displaymatrix'], Any]:
        """Cast needed video metadata fields to other types than the default str."""
        ...
    


def ffmpeg_parse_infos(filename, check_duration=..., fps_source=..., decode_file=..., print_infos=...): # -> dict[str, Any]:
    """Get the information of a file using ffmpeg.

    Returns a dictionary with next fields:

    - ``"duration"``
    - ``"metadata"``
    - ``"inputs"``
    - ``"video_found"``
    - ``"video_fps"``
    - ``"video_n_frames"``
    - ``"video_duration"``
    - ``"video_bitrate"``
    - ``"video_metadata"``
    - ``"audio_found"``
    - ``"audio_fps"``
    - ``"audio_bitrate"``
    - ``"audio_metadata"``
    - ``"video_codec_name"``
    - ``"video_profile"``

    Note that "video_duration" is slightly smaller than "duration" to avoid
    fetching the incomplete frames at the end, which raises an error.

    Parameters
    ----------

    filename
      Name of the file parsed, only used to raise accurate error messages.

    infos
      Information returned by FFmpeg.

    fps_source
      Indicates what source data will be preferably used to retrieve fps data.

    check_duration
      Enable or disable the parsing of the duration of the file. Useful to
      skip the duration check, for example, for images.

    decode_file
      Indicates if the whole file must be read to retrieve their duration.
      This is needed for some files in order to get the correct duration (see
      https://github.com/Zulko/moviepy/pull/1222).
    """
    ...

