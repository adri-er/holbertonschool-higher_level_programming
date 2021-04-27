#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number = number * (-1)
    last_digit = number % 10
    last_digit = last_digit * (-1)
    number = number * (-1)
    message = "and is less than 6 and not 0"
    print("Last digit of {} is {} {}".format(number, last_digit, message))
else:
    last_digit = number % 10
    if (last_digit > 5):
        message = "and is greater than 5"
        print("Last digit of {} is {} {}".format(number, last_digit, message))
    elif (last_digit == 0):
        message = "and is 0"
        print("Last digit of {} is {} {}".format(number, last_digit, message))
    else:
        message = "and is less than 6 and not 0"
        print("Last digit of {} is {} {}".format(number, last_digit, message))
