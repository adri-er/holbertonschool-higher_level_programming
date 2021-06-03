#!/usr/bin/python3
""" This module has a unique function that ckecks if object
is from an instance. """


def is_same_class(obj, a_class):
    """ Checks if an object is from a class.

    Args:
        obj (instance): insatnces to check.
        a_class (class): class to see coincidence of object.

    """
    return (a_class == type(obj))
