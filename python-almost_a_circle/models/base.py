#!/usr/bin/python3
"""class Base is the base of all other classes in this project"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method convert list to json representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        j_str = json.dumps(list_dictionaries)
        return j_str

    @classmethod
    def save_to_file(cls, list_objs):
        """class method convert a JSON str to a file"""
        with open(cls.__name__ + ".json", mode="w") as j_file:
            j_list = []
            if list_objs is not None:
                for element in list_objs:
                    j_list.append(cls.to_dictionary(element))
            j_file.write(Base.to_json_string(j_list))
                
