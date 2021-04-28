def islower(c):
    for letter in c:
        if (97 <= ord(letter) < 123):
            continue
        else:
            return False
    return True
