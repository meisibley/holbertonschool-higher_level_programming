#!/usr/bin/python3
import calculator_1 as cal
a = 10
b = 5
print("{0} + {1} = {2}".format(a, b, cal.add(a, b)))
print("{0} - {1} = {2}".format(a, b, cal.sub(a, b)))
print("{0} * {1} = {2}".format(a, b, cal.mul(a, b)))
if b != 0:
    print("{0} / {1} = {2}".format(a, b, cal.div(a, b)))
