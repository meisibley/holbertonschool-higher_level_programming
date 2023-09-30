#!/usr/bin/python3
"""module class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """child class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """display the rectangle"""
        rect1 = "[Square] "
        rect2 = "({}) {}/{}".format(self.id, self.x, self.y)
        rect3 = " - {}".format(self.width)
        return rect1 + rect2 + rect3

    def update(self, *args, **kwargs):
        """update attributes"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """square dictionry"""
        sqr_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
        return sqr_dict
