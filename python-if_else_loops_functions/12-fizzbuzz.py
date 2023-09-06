#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if int(i % 3) == 0 and int(i % 5) == 0:
            print("FizzBuzz", end=" ")
        elif int(i % 3) == 0 and int(i % 5) != 0:
            print("Fizz", end=" ")
        elif int(i % 3) != 0 and int(i % 5) == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
