#!/usr/bin/python3
"""class Base is the base of all other classes in this project"""


class Base:
    """class Base for unittest"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init of base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
