#!/usr/bin/python3
"""a function returns the JSON representation of an object"""


def to_json_string(my_obj):
    """return the JSON representation of an object(string)"""
    
    import json
    j_string = json.dumps(my_obj)
    return j_string
