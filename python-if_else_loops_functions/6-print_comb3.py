#!/usr/bin/python3
for i in range(1, 80):
    if int(i / 10) < i % 10:
        print("{:02d}".format(i), end=", ")
print("{}".format(89))
