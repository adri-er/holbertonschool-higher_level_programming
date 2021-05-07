#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary:
        max_value = max(list(a_dictionary.values()))

        for key in a_dictionary.keys():
            if a_dictionary[key] == max_value:
                return key

    return None
