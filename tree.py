from pathlib import Path
from typing import List
import os


def get_sorted_subtitems(dirname: str = ".") -> List[str]:
    return sorted([x.absolute() for x in Path(dirname).iterdir() if not x.is_dir()])


def get_sorted_dirs(dirname) -> List[str]:
    return sorted([x.absolute() for x in Path(dirname).iterdir() if x.is_dir()])


def get_sorted_items(dirname: str = ".") -> List[str]:
    return get_sorted_subtitems(dirname) + get_sorted_dirs(dirname)


def run(dirname: str = ".", indentation: int = 0) -> None:
    os.chdir(dirname)
    for item_ in get_sorted_items(dirname):
        if not item_.is_dir():
            print(" " * indentation, "-", item_.name.__str__())
        else:
            print(" " * indentation, "-", item_.name.__str__() + "\\")
            indentation_level_up = indentation
            run(item_.absolute().__str__(), indentation=indentation + len(item_.name.__str__()) + 2)
            indentation = indentation_level_up
