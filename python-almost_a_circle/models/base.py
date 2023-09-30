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
            f_list = []
            if list_objs:
                for ele in list_objs:
                    f_list.append(cls.to_dictionary(ele))
            j_file.write(Base.to_json_string(f_list))

    @staticmethod
    def from_json_string(json_string):
        """static method convert a json string to a list"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attrs already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        jfile = cls.__name__ + ".json"
        if not jfile:
            return []
        with open(jfile, "r") as jf:
            jstring = jf.read()
            pstring = cls.from_json_string(jstring)
        if cls:
            plist = []
            for ele in pstring:
                plist.append(cls.create(**ele))
        return plist
