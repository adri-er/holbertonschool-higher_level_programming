#!/usr/bin/python3
""" This module has a unique function that returns variables of an object."""


def lookup(obj):
    """ Returns list of variables of an object, attributes and methods.

    Args:
        obj (object): Object from which information is extracted.
    """
    return list(dir(obj))
