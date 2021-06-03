#!/usr/bin/python3
""" This module creates Base Geometry, Rectangle and Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherited class from rectangle.
    Is an inheritance from the Rectangle class.
    This class has the attirbute height and width. """

    def __init__(self, size):
        """ Initialization of a square.

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Determines the area of square. """
        return (self.__size * self.__size)
