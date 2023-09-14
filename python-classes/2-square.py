#!/usr/bin/python3
""" class Square: contains private instance attribute size"""

class Square:
    """ class Square"""

    def __init__(self, size=0):
        """size must be integer and not less than 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
