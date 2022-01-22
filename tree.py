from pathlib import Path
from typing import List
import os


def get_sorted_subtitems(dirname: str = ".") -> List[str]:
    """
    Description:
    -- get not directory items present in the given directory
    :param: dirname
    :type dirname: str
    :return: list of not directory items
    :rtype: List[str]
    """
    return sorted([x for x in Path(dirname).iterdir() if not x.is_dir()])


def get_sorted_dirs(dirname) -> List[str]:
    """
    Description:
    -- get directories present in the given directory
    :param: dirname
    :type dirname: str
    :return: list of directory items
    :rtype: List[str]
    """
    return sorted([x.absolute() for x in Path(dirname).iterdir() if x.is_dir()])


def get_sorted_items(dirname: str = ".") -> List[str]:
    """
    Description:
    -- get all items (directories and not) present in the given directory
    :param: dirname
    :type dirname: str
    :return: list of directory items
    :rtype: List[str]
    """
    return get_sorted_subtitems(dirname) + get_sorted_dirs(dirname)


def run(dirname: str = ".", indentation: int = 0) -> None:
    """
    Description:
    -- run tree aplication
    :param: dirname
    :type dirname: str
    :return: nothing
    """
    os.chdir(dirname)
    _dir = "."
    for item_ in get_sorted_items(_dir):
        if not item_.is_dir():
            print(" " * indentation, "-", item_.name)
        else:
            print(" " * indentation, "-", item_.name + "\\")
            indentation_level_up = indentation
            run(item_.absolute(), indentation=indentation + len(item_.name) + 2)
            indentation = indentation_level_up
