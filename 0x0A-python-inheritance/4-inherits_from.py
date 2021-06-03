#!/usr/bin/python3
""" This module has a unique function that ckecks if object
is from an inhereted class. """


def inherits_from(obj, a_class):
    """ Checks if an object is from an inherited class.

    Args:
        obj (instance): instance to check.
        a_class (class): class to see coincidence of object.

    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
