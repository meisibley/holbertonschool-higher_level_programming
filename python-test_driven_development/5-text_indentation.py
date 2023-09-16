#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """text must be a string, no space at the beginning or end of each line"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        ntxt = text
        for i in range(len(text)):
            ntxt = ntxt.replace(". ", ".", 1)
            ntxt = ntxt.replace("? ", "?", 1)
            ntxt = ntxt.replace(": ", ":", 1)
        for j in range(len(ntxt)):
            if ntxt[j - 1] != "." and ntxt[j - 1] != "?" and ntxt[j - 1] != ":":
                print("{}".format(ntxt[j]), end="")
            else:
                print("\n\n{}".format(ntxt[j]), end="")
