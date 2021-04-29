#!/usr/bin/python3
from sys import argv,exit
import calculator_1 as calc

if __name__ == "__main__":
    if (len(argv) != 4):
       print("Usage: ./100-my_calculator.py <a> <operator> <b>")
       exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if (operator == "+"):
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif (operator == "-"):
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif (operator == "*"):
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif (operator == "/"):
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
