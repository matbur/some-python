"""
Module implements tools used in this application.
"""

import os
import re


def join_path(*paths):
    return os.path.join(*paths)


def is_file(filename):
    return os.path.isfile(filename)


def read_file(filename):
    content = []
    err = None

    try:
        with open(filename) as f:
            content = f.readlines()
    except IOError as err:
        pass

    return strip_lines(content), err


def strip_lines(lines):
    if not isinstance(lines, (list, tuple)):
        lines = [lines]

    def strip(line):
        try:
            return line.strip()
        except AttributeError:
            return line

    return map(strip, lines)


def get_number(nr):
    return nr.split('/')[-1].split('.')[0]


def is_image(text, base):
    match = re.match('\[img\](?P<name>.*)\[/img\]', text)
    if not match:
        return False

    filename = match.group('name')
    filename = join_path(base, filename)
    return is_file(filename)


def get_img_path(is_img, text, base):
    if is_img:
        return join_path(base, text[5:-6])
    return ''
