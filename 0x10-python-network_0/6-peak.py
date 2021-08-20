#!/usr/bin/python3
""" This module contains a function that returns a peak """


def find_peak(list_of_integers):
    """ Finds a peak in a list of integers """
    answer = None
    i = 0
    length = len(list_of_integers)

    while (i < length - 1):
        if i + 1 < length - 1:
            if list_of_integers[i + 1] <= list_of_integers[i] and i - 1 < 0:
                answer = list_of_integers[i]
                break
            if i - 1 > 0:
                if list_of_integers[i + 1] <= list_of_integers[i] and list_of_integers[i - 1] <= list_of_integers[i]:
                    answer = list_of_integers[i]
                    break
        i += 1
        return answer
