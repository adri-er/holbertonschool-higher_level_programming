#!/usr/bin/python3
""" Module with unique file that prints pascal triangle"""


def pascal_triangle(n):
    """Prints pascal triangle

    Args:
        n (int): size of the pascal
    """
    if n <= 0:
        return []

    answer = []
    for i in range(n):
        intermediate = []
        if i == 0:
            intermediate.append(1)
        else:
            for j in range(i):
                if j == 0:
                    intermediate.append(1)

                elif j <= i - 1:
                    before = answer[i - 1][j - 1]
                    current = answer[i - 1][j]
                    intermediate.append(before + current)
            intermediate.append(1)
        answer.append(intermediate)
    return answer
