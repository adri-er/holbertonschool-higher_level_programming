#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    printed = 0

    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            printed += 1
        print("")
    except IndexError:
        print("")
    return printed
