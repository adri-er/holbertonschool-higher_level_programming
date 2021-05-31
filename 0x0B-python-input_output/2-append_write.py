#!/usr/bin/python3
"""
In this module a single function that appends a string to a file is created.
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): String with the name of the file.
        text (str): String to append in the file.

    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
