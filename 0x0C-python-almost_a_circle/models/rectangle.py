#!/usr/bin/python3
""" This module an inherite class, Rectangle, is created """
from models.base import Base


# Check what value can be (coord negatives and all can they be floats?)
class Rectangle(Base):
    """ Inherited class that models a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the values of a rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): horizontal coordinate of rectangle location.
            y (int): vertical coordinate of rectangle location.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Return the value of the width. """
        return self.__width

    @width.setter
    def width(self, width):
        """ Assign a value to the width.

        Arg:
            width (int): width of the rectangle.
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ Return the value of the height. """
        return self.__height

    @height.setter
    def height(self, height):
        """ Assign a value to the height. 

        Arg:
            height (int): Height of the rectangle.
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """ Return the value of x. """
        return self.__x

    @x.setter
    def x(self, x):
        """ Assigns a value to x coordinate.

        Args:
            x (int): horixontal coordinate of rectangle location. 
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ Return the value of y. """
        return self.__y

    @y.setter
    def y(self, y):
        """ Assigns a value to y coordinate.

        Args:
            y (int): vertical coordinate of location of rectangle.
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ Determines the area of a rectangle. """
        return self.__height * self.__width

    def display(self):
        """ Prints the rectangle in the stdout. """
        print("\n"*self.__y, end="")
        for i in range(self.__height):
            print(' '*self.__x, end="")
            print('#'*self.__width)

    def __str__(self):
        """ Returns the structure of desired string. """
        msg = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        msg = msg + " - {}/{}".format(self.__width, self.__height)
        return msg

    def update(self, *args, **kwargs):
        """Updates the attributes of current rectangle

        Args:
            args (list): array with the new values of id, width, height, x, y.
            kwargs (dictionary): array of new values with keys.
        """
        keys = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) > 0:
            if len(args) > len(keys):
                limit = len(keys)
            else:
                limit = len(args)
            for i in range(limit):
                setattr(self, keys[i], args[i])
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key in keys:
                        setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of Rectangle object. """

        dictionary = {"id": self.id, "width": self.__width,
                      "height": self.__height, "x": self.__x, "y": self.__y}
        return dictionary
