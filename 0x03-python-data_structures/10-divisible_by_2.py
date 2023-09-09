#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ver_list = []
    for i in my_list:
        if i % 2 == 0:
            ver_list.append(True)
        else:
            ver_list.append(False)
    return ver_list
