#!/usr/bin/python3
"""
In this module a single function that creates a class and has
method to print dict represenattion.
"""

class Student:
    """ Class that represents students.

    Attributes:
        first_name (str): First name of the student
        last_name (str): Last name of the student
        age (int): Age of the student. 
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__