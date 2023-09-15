#!/usr/bin/python3
"""Write a class Square that defines a squre"""


class Square:
    """private instance attribute: __size"""

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.__size = value
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        """initialize"""
        self.__size = size

    def area(self):
        """gets area"""
        return self.__size ** 2

