"""
This type stub file was generated by pyright.
"""

"""
Module for reading, writing and manipulating
Toolbox databases and settings files.
"""
class StandardFormat:
    """
    Class for reading and processing standard format marker files and strings.
    """
    def __init__(self, filename=..., encoding=...) -> None:
        ...
    
    def open(self, sfm_file): # -> None:
        """
        Open a standard format marker file for sequential reading.

        :param sfm_file: name of the standard format marker input file
        :type sfm_file: str
        """
        ...
    
    def open_string(self, s): # -> None:
        """
        Open a standard format marker string for sequential reading.

        :param s: string to parse as a standard format marker input file
        :type s: str
        """
        ...
    
    def raw_fields(self): # -> Generator[tuple[str | Any, str], Any, None]:
        """
        Return an iterator that returns the next field in a (marker, value)
        tuple. Linebreaks and trailing white space are preserved except
        for the final newline in each field.

        :rtype: iter(tuple(str, str))
        """
        ...
    
    def fields(self, strip=..., unwrap=..., encoding=..., errors=..., unicode_fields=...): # -> Generator[tuple[str | Any, str], Any, None]:
        """
        Return an iterator that returns the next field in a ``(marker, value)``
        tuple, where ``marker`` and ``value`` are unicode strings if an ``encoding``
        was specified in the ``fields()`` method. Otherwise they are non-unicode strings.

        :param strip: strip trailing whitespace from the last line of each field
        :type strip: bool
        :param unwrap: Convert newlines in a field to spaces.
        :type unwrap: bool
        :param encoding: Name of an encoding to use. If it is specified then
            the ``fields()`` method returns unicode strings rather than non
            unicode strings.
        :type encoding: str or None
        :param errors: Error handling scheme for codec. Same as the ``decode()``
            builtin string method.
        :type errors: str
        :param unicode_fields: Set of marker names whose values are UTF-8 encoded.
            Ignored if encoding is None. If the whole file is UTF-8 encoded set
            ``encoding='utf8'`` and leave ``unicode_fields`` with its default
            value of None.
        :type unicode_fields: sequence
        :rtype: iter(tuple(str, str))
        """
        ...
    
    def close(self): # -> None:
        """Close a previously opened standard format marker file or string."""
        ...
    


class ToolboxData(StandardFormat):
    def parse(self, grammar=..., **kwargs): # -> Element[str]:
        ...
    


_is_value = ...
def to_sfm_string(tree, encoding=..., errors=..., unicode_fields=...): # -> LiteralString:
    """
    Return a string with a standard format representation of the toolbox
    data in tree (tree can be a toolbox database or a single record).

    :param tree: flat representation of toolbox data (whole database or single record)
    :type tree: ElementTree._ElementInterface
    :param encoding: Name of an encoding to use.
    :type encoding: str
    :param errors: Error handling scheme for codec. Same as the ``encode()``
        builtin string method.
    :type errors: str
    :param unicode_fields:
    :type unicode_fields: dict(str) or set(str)
    :rtype: str
    """
    ...

class ToolboxSettings(StandardFormat):
    """This class is the base class for settings files."""
    def __init__(self) -> None:
        ...
    
    def parse(self, encoding=..., errors=..., **kwargs): # -> Element[str]:
        """
        Return the contents of toolbox settings file with a nested structure.

        :param encoding: encoding used by settings file
        :type encoding: str
        :param errors: Error handling scheme for codec. Same as ``decode()`` builtin method.
        :type errors: str
        :param kwargs: Keyword arguments passed to ``StandardFormat.fields()``
        :type kwargs: dict
        :rtype: ElementTree._ElementInterface
        """
        ...
    


def to_settings_string(tree, encoding=..., errors=..., unicode_fields=...): # -> LiteralString:
    ...

def remove_blanks(elem): # -> None:
    """
    Remove all elements and subelements with no text and no child elements.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    """
    ...

def add_default_fields(elem, default_fields): # -> None:
    """
    Add blank elements and subelements specified in default_fields.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    :param default_fields: fields to add to each type of element and subelement
    :type default_fields: dict(tuple)
    """
    ...

def sort_fields(elem, field_orders): # -> None:
    """
    Sort the elements and subelements in order specified in field_orders.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    :param field_orders: order of fields for each type of element and subelement
    :type field_orders: dict(tuple)
    """
    ...

def add_blank_lines(tree, blanks_before, blanks_between): # -> None:
    """
    Add blank lines before all elements and subelements specified in blank_before.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    :param blank_before: elements and subelements to add blank lines before
    :type blank_before: dict(tuple)
    """
    ...

def demo(): # -> None:
    ...

if __name__ == "__main__":
    ...
