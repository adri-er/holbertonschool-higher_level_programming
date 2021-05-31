#!/usr/bin/python3
"""
In this module a single function that returns an object JSON.
"""
import json


def from_json_string(my_str):
    """ Returns an object from a JSON. Deserializes.

    Args:
        my_str (str): String to deserialize.

    """
    return json.loads(my_str)
