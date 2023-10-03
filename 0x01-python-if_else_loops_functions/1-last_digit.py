#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_number = abs(number) %10
if number < 0
    last_number = -last_number
if last_number > 5:
    print(f"Last digit of {number:d} is {last_number:d} and is greater than 5")
elif last_number is 0:
    print(f"Last digit of {number:d} is {last_number:d} and is 0")
else:
    print(f"Last digit of {number:d} is {last_number:d} and is less than 6 and not 0")
