#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a2 = tuple_a + (0, 0)
    tuple_b2 = tuple_b + (0, 0)

    first = tuple_a2[0] + tuple_b2[0]
    second = tuple_a2[1] + tuple_b2[1]
    return (first, second)
