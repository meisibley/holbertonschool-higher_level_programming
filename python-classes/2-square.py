#!/usr/bin/python3
""" class Square: contains private instance attribute 'size'"""

class Square:
    """ define 'size', it must be integer and not less than 0"""

    def __init__(self, __size=0):
        if isinstance(__size, int) is False:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
