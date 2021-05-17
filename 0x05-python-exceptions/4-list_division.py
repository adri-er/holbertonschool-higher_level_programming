#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(0, list_length):
        message = ""
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            new_list.append(0)
            message += "wrong type\n"
        except ZeroDivisionError:
            new_list.append(0)
            message += "division by 0\n"
        except IndexError:
            new_list.append(0)
            message += "out of range\n"
        finally:
            print("{}".format(message), end="")

    return new_list
