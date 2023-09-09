#!/usr/bin/python3
def no_c(my_string):
    no_c_str = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        else:
            no_c_str += c
    return no_c_str
