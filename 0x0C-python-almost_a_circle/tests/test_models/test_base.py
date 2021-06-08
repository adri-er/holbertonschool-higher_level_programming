#!/usr/bin/python3
""" In this module, testing related to Base class will be done. """
import unittest
from models.base import Base


def setUpModule():
    """ Sets up the module by restarting the counter. """
    Base.__nb_objects = 0


class TestBase(unittest.TestCase):
    """ Test the base class """

    def test_init(self):
        """ Test cases of normal initialization """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(2)
        self.assertEqual(b2.id, 2)

        b3 = Base()  # CHECK THIS CASE that two can be same if choose that num
        self.assertEqual(b3.id, 2)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_failure(self):
        """ Test cases additional parameter is passed. """
        with self.assertRaises(TypeError):
            b5 = Base(2, 3)

        with self.assertRaises(ValueError):
            b6 = Base(-1)

        with self.assertRaises(ValueError):
            b7 = Base(0)
