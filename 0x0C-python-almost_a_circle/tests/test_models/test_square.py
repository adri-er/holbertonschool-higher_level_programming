#!/usr/bin/python3
""" In this module, testing related to Base class will be done. """
import unittest
import sys
from io import StringIO
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """ Test the Square class """

    def tearDown(self):
        """ Create environment """
        Base.reset_nb()

    def test_init(self):
        """ Test cases of normal initialization """

        # 4 parameters
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, 4)

        # 3 parameters
        s2 = Square(1, 2, 3)
        self.assertEqual(s2.id, 1)

        # 2 parameters
        s3 = Square(3, 5)
        self.assertEqual(s3.id, 2)

        # 1 parameters
        s4 = Square(1)
        self.assertEqual(s4.id, 3)

    def test_failure_parameters(self):
        """ Cases additional or none parameters are passed. """

        # MESSAGE OR JUST RAISE?
        # None parameters
        with self.assertRaises(TypeError):
            s5 = Square()

        # More than required
        with self.assertRaises(TypeError):
            s6 = Square(1, 2, 3, 4, 5)

    def test_failure_value_args(self):
        """ Test cases invalid value of args, negatives or zeros. """

        # Negatives values in dimension or id
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s7 = Square(-1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s8 = Square(1, -1, 2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s9 = Square(1, 1, -2)

        # Value zero in dimension
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s10 = Square(0, 1)

    def test_failure_type_args(self):
        """ Test cases invalid args are passed, types of data. """

        # LIST
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s11 = Square([1])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s12 = Square(1, [1])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s13 = Square(1, 2, [1])

        # FLOAT
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s14 = Square(1.1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s15 = Square(1, 1.1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s16 = Square(1, 2, 1.1)

        # STRING
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s17 = Square("1")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s18 = Square(1, "1")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s19 = Square(1, 2, "1")

        # DICTIONARY
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s20 = Square({1: 1})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s21 = Square(1, {1: 1})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s22 = Square(1, 2, 1.1)

    def test_setter_getter(self):
        """ Test setting and getting a new value. """

        # Functionals
        s22 = Square(1)
        self.assertEqual(s22.size, 1)

        s22.size = 3
        self.assertEqual(s22.size, 3)

        # Non-functionals
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s22.size = 3.1

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s22.size = "3"

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s22.size = {1}

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s22.size = [2]

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s22.size = 0

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s22.size = -1

    def test_area(self):
        """ Test cases of normal use of area method. """

        # 1 parameters
        s23 = Square(3)
        self.assertEqual(s23.area(), 9)

        # 2 parameters
        s24 = Square(3, 4)
        self.assertEqual(s24.area(), 9)

        # 3 parameters
        s25 = Square(3, 5, 2)
        self.assertEqual(s25.area(), 9)

        # 4 parameters
        s26 = Square(3, 6, 7, 2)
        self.assertEqual(s26.area(), 9)

    def test_display(self):
        """ Test case to display the rectangle. """

        # 1 parameter
        out = StringIO()
        sys.stdout = out
        s27 = Square(1)
        s27.display()
        output = out.getvalue()
        self.assertEqual(output, "#\n")

        # 2 parameters
        out = StringIO()
        sys.stdout = out
        s28 = Square(2, 2)
        s28.display()
        output = out.getvalue()
        self.assertEqual(output, "  ##\n  ##\n")

        # 3 parameters
        out = StringIO()
        sys.stdout = out
        s29 = Square(3, 3, 2)
        s29.display()
        output = out.getvalue()
        self.assertEqual(output, "\n\n   ###\n   ###\n   ###\n")

        # 4 parameters
        out = StringIO()
        sys.stdout = out
        s30 = Square(3, 3, 2, 192)
        s30.display()
        output = out.getvalue()
        self.assertEqual(output, "\n\n   ###\n   ###\n   ###\n")

    def test_print_object(self):
        """ Test case to print Square info. """

        # 1 parameter
        out = StringIO()
        sys.stdout = out
        s31 = Square(3)
        print(s31)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (1) 0/0 - 3\n")

        # 2 parameters
        out = StringIO()
        sys.stdout = out
        s32 = Square(3, 5)
        print(s32)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (2) 5/0 - 3\n")

        # 3 parameters
        out = StringIO()
        sys.stdout = out
        s33 = Square(3, 5, 8)
        print(s33)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (3) 5/8 - 3\n")

        # 4 parameters
        out = StringIO()
        sys.stdout = out
        s33 = Square(3, 5, 8, 99)
        print(s33)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (99) 5/8 - 3\n")

    def test_update(self):
        """ Test case to update rectangles attributes. """

        # UPDATE NONE
        out = StringIO()
        sys.stdout = out
        s34 = Square(10, 10, 10, 10)
        s34.update()
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (10) 10/10 - 10\n")

        # UPDATE ARGS
        # update 1 parameter (id)
        out = StringIO()
        sys.stdout = out
        s34.update(98)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 10/10 - 10\n")

        # update 2 parameter (id, size)
        out = StringIO()
        sys.stdout = out
        s34.update(98, 5)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 10/10 - 5\n")

        # update 3 parameter (id, size, x)
        out = StringIO()
        sys.stdout = out
        s34.update(98, 5, 7)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 7/10 - 5\n")

        # update 4 parameter (id, size, x, y)
        out = StringIO()
        sys.stdout = out
        s34.update(98, 5, 7, 9)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 7/9 - 5\n")

        # more than 4 parameters passed (ignores the rest)
        out = StringIO()
        sys.stdout = out
        s34.update(89, 51, 71, 91, 10)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (89) 71/91 - 51\n")

        # UPDATE KWARGS
        # update 1 param (id)
        out = StringIO()
        sys.stdout = out
        s34.update(id=98)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 71/91 - 51\n")

        # update 2 parameters (id, size)
        out = StringIO()
        sys.stdout = out
        s34.update(size=20, id=98)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 71/91 - 20\n")

        # update 3 parameters (id, size, x)
        out = StringIO()
        sys.stdout = out
        s34.update(size=20, id=98, x=3)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 3/91 - 20\n")

        # update 4 parameters (id, size, x, y)
        out = StringIO()
        sys.stdout = out
        s34.update(y=7, id=98, size=20, x=3)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 3/7 - 20\n")

        # update more than 4 parameters (id, size, x, y, depth)
        out = StringIO()
        sys.stdout = out
        s34.update(y=7, id=98, size=20, depth=27, x=3)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (98) 3/7 - 20\n")

        # UPDATE having both cases
        out = StringIO()
        sys.stdout = out
        s34.update(500, y=17, id=103, size=200, depth=270, x=93)
        print(s34)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (500) 3/7 - 20\n")

        # UPDATE with errors
        # error with size (id, size)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s34.update(500, 3.1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s34.update(500, -1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s34.update(500, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s34.update(size=3.1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s34.update(size=-1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s34.update(size=0)

        # error with x (id, size, x)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s34.update(500, 10, 3.1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s34.update(500, 10, -1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s34.update(x=3.1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s34.update(x=-1)

        # error with y (id, size, x, y)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s34.update(500, 10, 10, 3.1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s34.update(500, 10, 10, -1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s34.update(y=3.1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s34.update(y=-1)
