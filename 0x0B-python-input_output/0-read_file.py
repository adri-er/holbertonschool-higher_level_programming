#!/usr/bin/python3
"""
In this module a single function that reads a file is created.
"""


def read_file(filename=""):
    """ Reads a text file in UTF8 and prints it.

    Args:
        filename (str): String with the name of the file.

    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
