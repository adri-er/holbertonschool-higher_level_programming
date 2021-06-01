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
        """ Initializes the class. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary of the class attributes. """
        if attrs is None:
            return self.__dict__

        is_list_string = True
        for elem in attrs:
            if not isinstance(elem, str):
                is_list_string = False
                break

        answer = {}
        if is_list_string:
            for i in attrs:
                if i in list(self.__dict__.keys()):
                    answer[i] = self.__dict__[i]
                else:
                    continue
            return answer
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the students instance. """
        for attribute in list(self.__dict__.keys()):
            self.attribute = json[attribute]
