#!/usr/bin/python3
def print_last_digit(number):
    last = str(number)[-1]
    print("{}".format(last), end="")
    return (int(last))
