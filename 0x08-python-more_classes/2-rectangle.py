#!/usr/bin/python3
""" In this module a Rectangle class is created and it defines a rectangle.

Attributes:
     width (int): width of the rectangle object.
     height (int): height of the rectangle object.

Example:
   In this example a rectangle will be created (rec_1) with a specific
   width and height.
       rec_1 = Rectangle(2, 3)
       rec_2 = Rectangle(10, 20)

"""


class Rectangle:
    """ Defines a rectangle instance. """

    def __init__(self, width=0, height=0):
        """ Inititalizes a rectangle instance with the height and width.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the value of the width of a Rectangle instance. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of the width to a Rectangle instance.

        Args:
            value (int): Value of the Rectangles instance width.

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Gets the value of the height of a Rectangle instance. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of the height to a Rectangle instance.

        Args:
            value (int): Value of the Rectangles instance height.

        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the Rectangle instance. """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of the Rectangles instance. """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
