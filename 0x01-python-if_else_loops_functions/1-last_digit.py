#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dig = abs(number) % 10
if number < 0:
    lst_dig = -lst_dig
else:
    lst_dig
if lst_dig < 6 and lst_dig != 0:
    print(f"Last digit of {number} is {lst_dig} and is less than 6 and not 0")
elif lst_dig > 5:
    print(f"Last digit of {number} is {lst_dig} and is greater then 5")
else:
    print("Last digit of {number} is {lst_dig} and is 0")
