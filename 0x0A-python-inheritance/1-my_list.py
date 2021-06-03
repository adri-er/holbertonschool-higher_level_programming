#!/usr/bin/python3
""" This module has a unique purpose and is creating a class. """


class MyList(list):
    """ Inherits from list. """

    def print_sorted(self):
        """ Prints sorted list. """
        print(sorted(self))
