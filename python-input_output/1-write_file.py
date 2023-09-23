#!/usr/bin/python3
"""write a string to a text file and returns the num of charaters written"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
