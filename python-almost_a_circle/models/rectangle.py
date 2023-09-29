#!/usr/bin/python3
"""class Rectangle inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """child class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validator(self, attribut, value):
        """attribute integer validate"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribut))
        if attribut == "width" and value <= 0:
            raise ValueError("{} must be > 0".format(attribut))
        if attribut == "height" and value <= 0:
            raise ValueError("{} must be > 0".format(attribut))
        if (attribut == "x" and value < 0) or (attribut == "y" and value < 0):
            raise ValueError("{} must be >= 0".format(attribut))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        self.___height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
