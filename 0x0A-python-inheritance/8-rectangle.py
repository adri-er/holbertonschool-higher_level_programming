#!/usr/bin/python3
""" This module creates an Base Geometry and Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that represents a rectangle.
    Inherits from Basegeometry, it can use its methods.
    BaseGeometry doesn't have attributes. """

    def __init__(self, width, height):
        """ Initialization method for a rectangle validating value.
        Args:
            width (int): integer represents the width
            height (int): integer represents the height
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
