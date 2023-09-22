#!/usr/bin/python3
"""module of BaseGeometry"""


class BaseGeometry:
    """module of BaseGeometry"""

    def area(self):
        """empty area() function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate input value"""

        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
