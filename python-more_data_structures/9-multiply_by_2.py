#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        b_dictionary = {}
        for x, y in a_dictionary.items():
            b_dictionary.update({x: y * 2})
        return b_dictionary
    else:
        return a_dictionary
