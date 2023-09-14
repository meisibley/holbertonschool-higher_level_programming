#!/usr/bin/python3
""" class Square: contains private instance attribute __size"""

class Square:
    """ class Square"""

    def __init__(self, size=0):
        """ init size, it must be integer and not less than 0"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
