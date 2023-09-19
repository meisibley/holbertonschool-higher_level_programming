#!/usr/bin/python3
"""class Rectangle defines width and height"""


class Rectangle:
    """Rectangle define width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initiation with width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """gets area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """gets perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            perime = 0
        else:
            perime = (self.__width + self.height) * 2
        return perime

    def __str__(self):
        """use given chars to make a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect_matrix = ""
            for h in range(self.__height - 1):
                rect_matrix += "{}".format(self.print_symbol) * self.__width
                rect_matrix += "\n"
            rect_matrix += "{}".format(self.print_symbol) * self.__width
        return rect_matrix

    def __repr__(self):
        """return a string of the rectangle to recreate a new instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare and return the biggerst rectangle based on areas"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
