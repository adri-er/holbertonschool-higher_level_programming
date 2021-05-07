#!/usr/bin/python3


def roman_to_int(roman_string):

    decimal = 0
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    roman_num["M"] = 1000

    if roman_string and type(roman_string) == str:
        for i in range(len(roman_string)):
            if i < len(roman_string) - 1:
                if roman_num[roman_string[i]] >= roman_num[roman_string[i+1]]:
                    decimal += roman_num[roman_string[i]]
                else:
                    decimal -= roman_num[roman_string[i]]
            else:
                decimal += roman_num[roman_string[i]]

    return decimal
