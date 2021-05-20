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
    """ Defines a rectangle instance.

    Attributes:
        width (int): width of a rectangle
        height (int): height of a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Inititalizes a rectangle instance with the height and width.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """ Prints the Rectangles instance with # """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect_print = ""
            for i in range(0, self.__height):
                rect_print += "#" * self.__width + "\n"
            return rect_print[0:-1]

    def __repr__(self):
        """ Returns a string representation of a rectangle able to recreate."""
        msg = "Rectangle" + "(" + str(self.__width)
        return msg + ", " + str(self.__height) + ")"

    def __del__(self):
        """Prints message when the last pointer to instance is deleted."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on area. """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_areas = {}
        rect_areas[rect_1] = rect_1.__width * rect_1.__height
        rect_areas[rect_2] = rect_2.__width * rect_2.__height
        if rect_areas[rect_1] >= rect_areas[rect_2]:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Creates a square of Rectangle class. """
        return cls(size, size)
