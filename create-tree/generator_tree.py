""" Module contains necessary functions to
    generate random tree with files and directories.
"""

import os
from os.path import join as join_path

from random_tree import RandomTree


def recognize_type(items, path=''):
    """ Function yields path with information if it file or dir.

        True if directory, False otherwise.
    """
    for item in items:
        if isinstance(item, str):
            new_path = join_path(path, item)
            yield new_path, False
            continue

        for dir_name, dir_content in item.items():
            new_path = join_path(path, dir_name)
            yield new_path, True
            yield from recognize_type(dir_content, path=new_path)


def create(name, is_dir):
    """ Function creates new file or directory depending on 'is_dir'.
    """
    if is_dir:
        create_dir(name)
    else:
        create_file(name)


def create_file(name):
    """ Function creates new file if none error occurred.
    """
    try:
        with open(name, 'w'):
            pass
    except (IsADirectoryError, NotADirectoryError):
        return


def create_dir(name):
    """ Function makes new directory if none error occurred.
    """
    try:
        os.mkdir(name)
    except (FileExistsError, NotADirectoryError):
        pass


def main():
    """ Function creates new tree with all files and directories.
    """
    tree = RandomTree(3, 3)

    for item in recognize_type(tree.get()):
        create(*item)

    print(tree.debug())


if __name__ == '__main__':
    main()
