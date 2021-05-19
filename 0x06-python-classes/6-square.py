#!/usr/bin/python3
"""
This module defines a class Square based on a previous document.
"""


class Square:
    """The Square class defines a square.

    Attributes:
       None.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Inititialization of the attributes the Square class has.
        Args:
           size (int): Size of the square, private attribute.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets the value of the private attribute size. """
        return self.__size

    @size.setter
    def size(self, size):
        """ Sets the size of the instance considering exceptions """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """ Gets the value of the private attribute position. """
        return self.__position

    @position.setter
    def position(self, position):
        """ Sets the position of the square. """
        if len(position) != 2 or type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) != int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """ Returns the current square instance area """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character #. """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
