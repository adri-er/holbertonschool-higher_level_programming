#!/usr/bin/python3
"""
In this module a single function that returns dictionary
description of an object.
"""
import json


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (class) : Instance of a class.

    """
    return obj.__dict__
