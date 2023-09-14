#!/usr/bin/python3
""" class Square: contains private instance attribute 'size'"""

class Square:
    """ define 'size', it must be integer and not less than 0"""

    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
