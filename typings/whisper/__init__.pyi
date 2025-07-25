"""
This type stub file was generated by pyright.
"""

import itertools
import operator
import os
import platform
import re
import struct
import sys
import time
import fcntl
import ctypes
import ctypes.util
from os import POSIX_FADV_RANDOM, posix_fadvise

izip = ...
ifilter = ...
if sys.version_info >= (3, 0):
  xrange = range
CAN_LOCK = ...
CAN_FALLOCATE = ...
if sys.version_info >= (3, 0):
  ...
else:
  ...
CAN_FADVISE = ...
fallocate = ...
if CAN_FALLOCATE:
  libc_name = ...
  libc = ...
  c_off64_t = ctypes.c_int64
  c_off_t = ...
  _fallocate = ...
LOCK = ...
CACHE_HEADERS = ...
AUTOFLUSH = ...
FADVISE_RANDOM = ...
BUFFERING = ...
__headerCache = ...
longFormat = ...
longSize = ...
floatFormat = ...
floatSize = ...
valueFormat = ...
valueSize = ...
pointFormat = ...
pointSize = ...
metadataFormat = ...
metadataSize = ...
archiveInfoFormat = ...
archiveInfoSize = ...
aggregationTypeToMethod = ...
aggregationMethodToType = ...
aggregationMethods = ...
endBlock = ...
UnitMultipliers = ...
def getUnitString(s): # -> Literal['seconds', 'minutes', 'hours', 'days', 'weeks', 'years']:
  ...

def parseRetentionDef(retentionDef): # -> tuple[int, int]:
  ...

class WhisperException(Exception):
  """Base class for whisper exceptions."""
  ...


class InvalidConfiguration(WhisperException):
  """Invalid configuration."""
  ...


class InvalidAggregationMethod(WhisperException):
  """Invalid aggregation method."""
  ...


class InvalidTimeInterval(WhisperException):
  """Invalid time interval."""
  ...


class InvalidXFilesFactor(WhisperException):
  """Invalid xFilesFactor."""
  ...


class TimestampNotCovered(WhisperException):
  """Timestamp not covered by any archives in this database."""
  ...


class CorruptWhisperFile(WhisperException):
  def __init__(self, error, path) -> None:
    ...
  
  def __repr__(self): # -> LiteralString:
    ...
  
  def __str__(self) -> str:
    ...
  


def disableDebug(): # -> None:
  """ Disable writing IO statistics to stdout """
  ...

def enableDebug(): # -> None:
  """ Enable writing IO statistics to stdout """
  class open:
    ...
  
  

def setXFilesFactor(path, xFilesFactor):
  """Sets the xFilesFactor for file in path

  path is a string pointing to a whisper file
  xFilesFactor is a float between 0 and 1

  returns the old xFilesFactor
  """
  ...

def setAggregationMethod(path, aggregationMethod, xFilesFactor=...):
  """Sets the aggregationMethod for file in path

  path is a string pointing to the whisper file
  aggregationMethod specifies the method to use when propagating data (see
  ``whisper.aggregationMethods``)
  xFilesFactor specifies the fraction of data points in a propagation interval
  that must have known values for a propagation to occur. If None, the
  existing xFilesFactor in path will not be changed

  returns the old aggregationMethod
  """
  ...

def validateArchiveList(archiveList): # -> None:
  """ Validates an archiveList.
  An ArchiveList must:
  1. Have at least one archive config. Example: (60, 86400)
  2. No archive may be a duplicate of another.
  3. Higher precision archives' precision must evenly divide all lower
     precision archives' precision.
  4. Lower precision archives must cover larger time intervals than higher
     precision archives.
  5. Each archive must have at least enough points to consolidate to the next
     archive

  Returns True or False
  """
  ...

def create(path, archiveList, xFilesFactor=..., aggregationMethod=..., sparse=..., useFallocate=...):
  """create(path,archiveList,xFilesFactor=0.5,aggregationMethod='average')

  path               is a string
  archiveList        is a list of archives, each of which is of the form
                     (secondsPerPoint, numberOfPoints)
  xFilesFactor       specifies the fraction of data points in a propagation interval
                     that must have known values for a propagation to occur
  aggregationMethod  specifies the function to use when propagating data (see
                     ``whisper.aggregationMethods``)
  """
  ...

def aggregate(aggregationMethod, knownValues, neighborValues=...): # -> float:
  ...

def update(path, value, timestamp=..., now=...): # -> None:
  """
  update(path, value, timestamp=None)

  path is a string
  value is a float
  timestamp is either an int or float
  """
  ...

def file_update(fh, value, timestamp, now=...): # -> None:
  ...

def update_many(path, points, now=...): # -> None:
  """update_many(path,points)

path is a string
points is a list of (timestamp,value) points
"""
  ...

def file_update_many(fh, points, now=...): # -> None:
  ...

def info(path): # -> dict[str, Any] | None:
  """
  info(path)

  path is a string
  """
  ...

def fetch(path, fromTime, untilTime=..., now=..., archiveToSelect=...): # -> tuple[tuple[Any, Any, Any], Any] | tuple[tuple[Any, Any, Any], list[None]] | None:
  """fetch(path,fromTime,untilTime=None,archiveToSelect=None)

path is a string
fromTime is an epoch time
untilTime is also an epoch time, but defaults to now.
archiveToSelect is the requested granularity, but defaults to None.

Returns a tuple of (timeInfo, valueList)
where timeInfo is itself a tuple of (fromTime, untilTime, step)

Returns None if no data can be returned
"""
  ...

def file_fetch(fh, fromTime, untilTime, now=..., archiveToSelect=...): # -> tuple[tuple[Any, Any, Any], Any] | tuple[tuple[Any, Any, Any], list[None]] | None:
  ...

def merge(path_from, path_to, time_from=..., time_to=..., now=...): # -> None:
  """ Merges the data from one whisper file into another. Each file must have
  the same archive configuration. time_from and time_to can optionally be
  specified for the merge.
"""
  ...

def file_merge(fh_from, fh_to, time_from=..., time_to=..., now=...): # -> None:
  ...

def diff(path_from, path_to, ignore_empty=..., until_time=..., now=...): # -> list[Any]:
  """ Compare two whisper databases. Each file must have the same archive configuration """
  ...

def file_diff(fh_from, fh_to, ignore_empty=..., until_time=..., now=...): # -> list[Any]:
  ...

