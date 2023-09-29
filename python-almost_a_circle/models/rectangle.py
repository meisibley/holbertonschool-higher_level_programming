#!/usr/bin/python3
"""class Rectangle inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """child class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validator(self, attri, value):
        """attribute integer validate"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attri))
        if (attri == "width" and value <= 0):
            raise ValueError("{} must be > 0".format(attri))
        if (attri == "height" and value <= 0):
            raise ValueError("{} must be > 0".format(attri))
        if ((attri == "x" and value < 0) or (attri == "y" and value < 0)):
            raise ValueError("{} must be >= 0".format(attri))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator("height", value)
        self.___height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.integer_validator("y", value)
        self.__y = value
