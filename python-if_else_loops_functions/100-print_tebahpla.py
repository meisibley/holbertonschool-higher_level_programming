#!/usr/bin/python3
for i in reversed(range(65, 91, 2)):
    print("{}{}".format(chr(i + 33), chr(i)), end="")
