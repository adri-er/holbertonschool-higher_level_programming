#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    amount_args = len(sys.argv) - 1
    if (amount_args == 1):
        message = "argument:"
    elif (amount_args == 0):
        message = "arguments."
    else:
        message = "arguments:"
    print("{} {}".format(amount_args, message))
    for i in range(1, amount_args + 1):
        print("{}: {}".format(i, sys.argv[i]))
