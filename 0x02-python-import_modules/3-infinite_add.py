#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    amount_args = len(sys.argv)
    sum = 0
    for i in range(1, amount_args):
        sum += int(sys.argv[i])
    print("{}".format(sum))
