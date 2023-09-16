#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """size is the size length of the square, must be integer"""

    err1 = "size must be an integer"
    err2 = "size must be >= 0"
    if not isinstance(size, int):
        raise TypeError(err1)
    if size < 0:
        raise ValueError(err2)
    if isinstance(size, float) and size < 0:
        raise TypeError(err1)
    for i in range(size):
        print("{}".format("#") * size)
