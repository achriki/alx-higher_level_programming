#!/usr/bin/python3

def weight_average(my_list=[]):
    s = 0
    d = 0
    if len(my_list) == 0:
        return 0
    else:
        for tup in my_list:
            if len(tup) != 0:
                s += (tup[0] * tup[1])
                d += tup[1]
            else:
                continue
        return s / d
    return 0
