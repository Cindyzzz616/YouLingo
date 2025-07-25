"""
This type stub file was generated by pyright.
"""

from nltk.internals import deprecated

"""
Utility functions for the `twitterclient` module which do not require
the `twython` library to have been installed.
"""
HIER_SEPARATOR = ...
def extract_fields(tweet, fields): # -> list[Any]:
    """
    Extract field values from a full tweet and return them as a list

    :param json tweet: The tweet in JSON format
    :param list fields: The fields to be extracted from the tweet
    :rtype: list(str)
    """
    ...

def json2csv(fp, outfile, fields, encoding=..., errors=..., gzip_compress=...): # -> None:
    """
    Extract selected fields from a file of line-separated JSON tweets and
    write to a file in CSV format.

    This utility function allows a file of full tweets to be easily converted
    to a CSV file for easier processing. For example, just TweetIDs or
    just the text content of the Tweets can be extracted.

    Additionally, the function allows combinations of fields of other Twitter
    objects (mainly the users, see below).

    For Twitter entities (e.g. hashtags of a Tweet), and for geolocation, see
    `json2csv_entities`

    :param str infile: The name of the file containing full tweets

    :param str outfile: The name of the text file where results should be\
    written

    :param list fields: The list of fields to be extracted. Useful examples\
    are 'id_str' for the tweetID and 'text' for the text of the tweet. See\
    <https://dev.twitter.com/overview/api/tweets> for a full list of fields.\
    e. g.: ['id_str'], ['id', 'text', 'favorite_count', 'retweet_count']\
    Additionally, it allows IDs from other Twitter objects, e. g.,\
    ['id', 'text', 'user.id', 'user.followers_count', 'user.friends_count']

    :param error: Behaviour for encoding errors, see\
    https://docs.python.org/3/library/codecs.html#codec-base-classes

    :param gzip_compress: if `True`, output files are compressed with gzip
    """
    ...

@deprecated("Use open() and csv.writer() directly instead.")
def outf_writer_compat(outfile, encoding, errors, gzip_compress=...): # -> tuple[_writer, TextIOWrapper[_WrappedBuffer]]:
    """Get a CSV writer with optional compression."""
    ...

def json2csv_entities(tweets_file, outfile, main_fields, entity_type, entity_fields, encoding=..., errors=..., gzip_compress=...): # -> None:
    """
    Extract selected fields from a file of line-separated JSON tweets and
    write to a file in CSV format.

    This utility function allows a file of full Tweets to be easily converted
    to a CSV file for easier processing of Twitter entities. For example, the
    hashtags or media elements of a tweet can be extracted.

    It returns one line per entity of a Tweet, e.g. if a tweet has two hashtags
    there will be two lines in the output file, one per hashtag

    :param tweets_file: the file-like object containing full Tweets

    :param str outfile: The path of the text file where results should be\
        written

    :param list main_fields: The list of fields to be extracted from the main\
        object, usually the tweet. Useful examples: 'id_str' for the tweetID. See\
        <https://dev.twitter.com/overview/api/tweets> for a full list of fields.
        e. g.: ['id_str'], ['id', 'text', 'favorite_count', 'retweet_count']
        If `entity_type` is expressed with hierarchy, then it is the list of\
        fields of the object that corresponds to the key of the entity_type,\
        (e.g., for entity_type='user.urls', the fields in the main_fields list\
        belong to the user object; for entity_type='place.bounding_box', the\
        files in the main_field list belong to the place object of the tweet).

    :param list entity_type: The name of the entity: 'hashtags', 'media',\
        'urls' and 'user_mentions' for the tweet object. For a user object,\
        this needs to be expressed with a hierarchy: `'user.urls'`. For the\
        bounding box of the Tweet location, use `'place.bounding_box'`.

    :param list entity_fields: The list of fields to be extracted from the\
        entity. E.g. `['text']` (of the Tweet)

    :param error: Behaviour for encoding errors, see\
        https://docs.python.org/3/library/codecs.html#codec-base-classes

    :param gzip_compress: if `True`, output files are compressed with gzip
    """
    ...

def get_header_field_list(main_fields, entity_type, entity_fields): # -> list[str]:
    ...

