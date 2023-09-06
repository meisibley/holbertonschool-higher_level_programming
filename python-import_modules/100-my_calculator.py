#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != "/":
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
a = int(argv[1])
b = int(argv[3])
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if argv[2] == "+":
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    if argv[2] == "-":
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    if argv[2] == "*":
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    if argv[2] == "/" and b != 0:
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
