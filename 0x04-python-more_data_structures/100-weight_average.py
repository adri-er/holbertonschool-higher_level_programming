#!/usr/bin/python3


def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0

    numerator = sum(list(map(lambda x: x[0] * x[1], my_list)))
    denominator = sum(list(map(lambda x: x[1], my_list)))
    return numerator / denominator
