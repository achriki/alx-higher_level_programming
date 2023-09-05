#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dig = abs(number) % 10
init_str = "Last digit of"
if number < 0:
    lst_dig = -lst_dig
if lst_dig < 6 and lst_dig != 0:
   print("{} {} is {} and is less than 6 and not 0".format(init_str, number, lst_dig))
elif lst_dig > 5:
    print("{} {} is {} and is greater then 5".format(init_str, number, lst_dig))
else:
    print("{} {} is {} and is 0".format(init_str, number, lst_dig))
