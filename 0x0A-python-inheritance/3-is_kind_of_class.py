#!/usr/bin/python3
""" This module has a unique function that ckecks if object
is from an instance or inhereted class. """


def is_kind_of_class(obj, a_class):
    """ Checks if an object is from a class or subclass.

    Args:
        obj (instance): instance to check.
        a_class (class): class to see coincidence of object.

    """
    if (a_class == type(obj) or issubclass(type(obj), a_class)):
        return True
    return False
