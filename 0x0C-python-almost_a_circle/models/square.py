#!/usr/bin/python3
""" I this module the Square class is created, inherits from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a square. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes values of a square.

        Args:
            size (int): length of  side of the square.
            x (int): horizontal coordinate of square loctaion.
            y (int): vertical coordniate of square location.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the squares width/size. """
        return self.width

    @size.setter
    def size(self, size):
        """ Assigns value to width and height """
        if type(size) != int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size

    def __str__(self):
        "Arrange the print(object) text."
        msg = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        return msg + " - {}".format(self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of current square

        Args:
            args (list): array with the new values of id, width, height, x, y.
            kwargs (dictionary): array of new values with keys.
        """
        keys = ['id', 'size', 'x', 'y']
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
        """ Returns the dictionary representation of a Square object. """

        dict_att = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dict_att
