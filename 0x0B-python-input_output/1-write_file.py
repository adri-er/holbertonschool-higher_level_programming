#!/usr/bin/python3
"""
In this module a single function that writes a string is created.
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8) and returns the
    number of characters written:

    Args:
        filename (str): String with the name of the file.
        text (str): String to write in the file.

    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
