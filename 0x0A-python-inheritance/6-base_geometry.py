#!/usr/bin/python3
""" This module creates an empty class and non-funtional method."""


class BaseGeometry:
    """ Class that represents the base geometry. """

    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")
