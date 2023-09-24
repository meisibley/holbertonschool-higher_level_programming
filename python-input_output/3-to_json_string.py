#!/usr/bin/python3
"""a function returns the JSON representation of an object"""


import json
def to_json_string(my_obj):
    """return the JSON representation of an object(string)"""
    
    return json.dumps(my_obj)
