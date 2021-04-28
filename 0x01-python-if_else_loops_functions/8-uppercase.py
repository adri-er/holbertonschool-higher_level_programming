def uppercase(str):
    for letter in str:
        number = ord(letter)
        if (97 <= number < 123):
            number -= 32
        print("{}".format(chr(number)), end="")
    print("\n", end="")
