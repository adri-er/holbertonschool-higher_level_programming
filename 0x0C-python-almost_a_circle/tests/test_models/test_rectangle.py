#!/usr/bin/python3
""" In this module, testing related to Base class will be done. """
import unittest
from models.rectangle import Rectangle
from models.base import Base
# Check message or just exception raised?


def setUp():
    """ Sets up the module by restarting the counter. """
    Base.__nb_objects = 0


class TestRectangle(unittest.TestCase):
    """ Test the Rectangle class that inherits from Base. """

    def test_init(self):
        """ Test cases of normal initialization """

        # 5 parameters
        r2 = Rectangle(1, 2, 3, 4, 10)
        ans = [1, 2, 3, 4, 10]
        self.assertEqual(r2.id, ans[-1])
        # self.assertEqual([r2.__width, r2.__height,
        # r2.__x, r2.__y, r2.id], ans)

        # 4 parameters
        r3 = Rectangle(1, 2, 3, 4)
        ans = [2, 1, 2, 3, 1]
        self.assertEqual(r3.id, ans[-1])
        # self.assertEqual([r3.__width, r3.__height,
        # r3.__x, r3.__y, r3.id], ans)

        # 3 parameters
        r4 = Rectangle(1, 2, 3)
        ans = [1, 2, 3, 0, 2]
        self.assertEqual(r4.id, ans[-1])
        # self.assertEqual([r4.__width, r4.__height,
        # r4.__x, r4.__y, r4.id], ans)

        # 2 parameters
        r1 = Rectangle(3, 5)
        ans = [3, 5, 0, 0, 3]
        self.assertEqual(r1.id, ans[-1])
        # self.assertEqual([r1.__width, r1.__height,
        # r1.__x, r1.__y, r1.id], ans)

        # 5 parameters - Initialize in 0 x and y
        r2 = Rectangle(1, 2, 0, 0)
        ans = [1, 2, 0, 0, 4]
        self.assertEqual(r2.id, ans[-1])
        # self.assertEqual([r2.__width, r2.__height,
        # r2.__x, r2.__y, r2.id], ans)

    def test_failure_parameters(self):
        """ Cases additional, none or less parameters are passed. """

        # MESSAGE OR JUST RAISE?
        # None parameters
        with self.assertRaises(TypeError):
            r5 = Rectangle()

        # Less than required
        with self.assertRaises(TypeError):
            r6 = Rectangle(1)

        # More than required
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_failure_value_args(self):
        """ Test cases invalid value of args, negatives or zeros. """

        # Negatives values in dimensions or id
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r8 = Rectangle(-1, 1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r9 = Rectangle(1, -1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r10 = Rectangle(1, 1, -1, 2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r11 = Rectangle(1, 1, 1, -2)

        # Value zero in dimensions
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r12 = Rectangle(0, 1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r13 = Rectangle(1, 0)

    def test_failure_type_args(self):
        """ Test cases invalid args are passed, types of data. """

        # LIST
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r14 = Rectangle([1], 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r15 = Rectangle(1, [1])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r16 = Rectangle(1, 1, [1])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r17 = Rectangle(1, 1, 2, [0])

        # FLOAT
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r18 = Rectangle(1.1, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r19 = Rectangle(1, 1.1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r20 = Rectangle(1, 1, 1.2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r21 = Rectangle(1, 1, 2, 1.3)

        # STRING
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r22 = Rectangle("1", 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r23 = Rectangle(1, "1")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r24 = Rectangle(1, 1, "1")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r25 = Rectangle(1, 1, 2, "1")

        # DICTIONARY
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r26 = Rectangle({1: 1}, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r27 = Rectangle(1, {1: 1})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r28 = Rectangle(1, 1, {1: 1})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29 = Rectangle(1, 1, 2, {1: 1})

    def test_setter_getter(self):
        """ Test setting and getting a new value. """

        # Check if I can do this
        r29 = Rectangle(7, 8)  # 5
        self.assertEqual(r29.width, 7)

        # set width
        r29.width = 3
        # get width
        self.assertEqual(r29.width, 3)

        # set height
        r29.height = 3
        # get height
        self.assertEqual(r29.height, 3)

        # set x
        r29.x = 8
        # get x
        self.assertEqual(r29.x, 8)

        # set y
        r29.y = 8
        # get y
        self.assertEqual(r29.y, 8)

        # EXCEPTIONS when setting - value errors
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r29.width = -1

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r29.width = 0

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r29.height = -1

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r29.height = 0

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r29.x = -1

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r29.y = -1

        # EXCEPTIONS when setting - type errors
        # width
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = {1}

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = [1]

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = 1.1

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = "1"

        # height
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = {1}

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = [1]

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = 1.1

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = "1"

        # x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = {1}

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = [1]

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = 1.1

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = "1"

        # y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = {1}

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = [1]

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = 1.1

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = "1"

    def test_area(self):
        """ Test cases of normal use of area method. """

        # 2 parameters
        r30 = Rectangle(3, 2)
        self.assertEqual(r30.area(), 6)

        # 3 parameters
        r31 = Rectangle(3, 4, 2)
        self.assertEqual(r31.area(), 12)

        # 4 parameters
        r32 = Rectangle(3, 5, 2, 1)
        self.assertEqual(r32.area(), 15)

        # 5 parameters
        r33 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r33.area(), 56)

    def test_display(self):
        """ Test case to display the rectangle. """

        # 2 parameters
        r34 = Rectangle(3, 2)
        self.assertEqual(r34.display(), "###\n###\n###\n")

        # 3 parameters
        r35 = Rectangle(2, 3, 2)
        self.assertEqual(r35.display(), "  ##\n  ##\n  ##\n  ##\n")

        # 4 parameters
        r36 = Rectangle(3, 5, 2, 1)
        self.assertEqual(
            r36.display(), "\n  ###\n  ###\n  ###\n  ###\n  ###\n")

        # 5 parameters
        r37 = Rectangle(1, 2, 0, 0, 12)
        self.assertEqual(r37.display(), "#\n#\n")

    def test_print_object(self):
        """ Test case to print rectangle info. """

        # 2 parameters
        r38 = Rectangle(3, 2)
        self.assertEqual(print(r38), "[Rectangle] (12) 0/0 - 3/2")

        # 3 parameters
        r39 = Rectangle(2, 3, 2)
        self.assertEqual(print(r39), "[Rectangle] (13) 2/0 - 2/3")

        # 4 parameters
        r40 = Rectangle(3, 5, 2, 1)
        self.assertEqual(print(r40), "[Rectangle] (14) 2/1 - 3/5")

        # 5 parameters
        r41 = Rectangle(1, 2, 0, 0, 20)
        self.assertEqual(print(r41), "[Rectangle] (20) 0/0 - 1/2")

    def test_update(self):
        """ Test case to update rectangles attributes. """

        # UPDATE NONE
        r42 = Rectangle(10, 10, 10, 10)
        r42.update()
        self.assertEqual(print(r42), "[Rectangle] (15) 10/10 - 10/10")

        # UPDATE ARGS
        # update 1 parameter (id)
        r42.update(89)
        self.assertEqual(print(r42), "[Rectangle] (89) 10/10 - 10/10")

        # update 2 parameter (id, width)
        r42.update(89, 2)
        self.assertEqual(print(r42), "[Rectangle] (89) 10/10 - 2/10")

        # update 3 parameter (id, width, height)
        r42.update(89, 2, 3)
        self.assertEqual(print(r42), "[Rectangle] (89) 10/10 - 2/3")

        # update 4 parameter (id, width, height, x)
        r42.update(89, 2, 3, 4)
        self.assertEqual(print(r42), "[Rectangle] (89) 4/10 - 2/3")

        # update 5 parameter (id, width, height, x, y)
        r42.update(89, 2, 3, 4, 5)
        self.assertEqual(print(r42), "[Rectangle] (89) 4/5 - 2/3")

        # more than 5 parameters passed
        r42.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(print(r42), "[Rectangle] (89) 4/5 - 2/3")
        # Should the upper part be an error?? args length specific?

        # UPDATE KWARGS
        # update 2 parameter
        r42.update(height=1)
        self.assertEqual(print(r42), "[Rectangle] (89) 4/5 - 2/1")

        # update 2 parameters
        r42.update(height=1, width=1)
        self.assertEqual(print(r42), "[Rectangle] (89) 4/5 - 1/1")

        # update 3 parameters
        r42.update(height=1, width=1, x=2)
        self.assertEqual(print(r42), "[Rectangle] (89) 2/5 - 1/1")

        # update 4 parameters
        r42.update(height=1, width=1, x=2, y=3)
        self.assertEqual(print(r42), "[Rectangle] (89) 2/3 - 1/1")

        # update 5 parameters
        r42.update(height=1, width=1, x=2, y=3, id=90)
        self.assertEqual(print(r42), "[Rectangle] (90) 2/3 - 1/1")

        # update more tha 5 parameters
        r42.update(height=1, width=1, x=2, y=3, id=90, depth=90)
        self.assertEqual(print(r42), "[Rectangle] (90) 2/3 - 1/1")

        # UPDATE having both cases
        r42.update(201, height=3, width=2, x=4, y=7, id=98)
        self.assertEqual(print(r42), "[Rectangle] (201) 2/3 - 1/1")

        # UPDATE with errors
        # error with size (id, width)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r42.update(500, 3.1)

        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            r42.update(500, -1)

        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            r42.update(500, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r42.update(width=3.1)

        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            r42.update(width=-1)

        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            r42.update(width=0)

        # error with height (id, width, height)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r42.update(500, 3, 3.1)

        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            r42.update(500, 3, -1)

        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            r42.update(500, 3, 0)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r42.update(height=3.1)

        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            r42.update(height=-1)

        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            r42.update(height=0)

        # error with x (id, width, height, x)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r42.update(500, 10, 3, 3.1)

        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            r42.update(500, 10, 3, -1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r42.update(x=3.1)

        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            r42.update(x=-1)

        # error with y (id, width, height, x, y)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r42.update(500, 10, 10, 3.1)

        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            r42.update(500, 10, 10, -1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r42.update(y=3.1)

        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            r42.update(y=-1)

    def test_to_dictionary(self):
        """ Test function that returns a dictionary. """
        r43 = Rectangle(1, 2, 3, 4, 5)
        dictionary = "{'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}"
        self.assertEqual(str(r43.to_dictionary()), dictionary)
