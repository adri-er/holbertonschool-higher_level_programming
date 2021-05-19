#!/usr/bin/python3
"""
This module defines a class Square based on a previous document.
"""


class Square:
    """The Square class defines a square.

    Attributes:
       None.
    """
    def __init__(self, size=0):
        """ Inititialization of the attributes the Square class has.
        Args:
           size (int): Size of the square, private attribute.

        """
        self.set_size(size)

    def get_size(self):
        """ Gets the value of the private attribute size. """
        return self.__size

    def set_size(self, size):
        """ Sets the size of the instance considering exceptions """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
