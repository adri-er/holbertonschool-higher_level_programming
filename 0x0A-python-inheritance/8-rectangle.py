#!/usr/bin/python3
""" This module creates an Base Geometry and Rectangle class."""


class BaseGeometry:
    """ Class that represents the base geometry. """

    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class that represents a rectangle.
    Inherits from basegeometry, it can use its methods.
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
