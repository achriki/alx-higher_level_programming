#!/usr/bin/python3:
def complex_delete(a_dictionary, value):
    for k in list(a_dictionary):
        if value == a_dictionary.get(k):
            del a_dictionary[k]
        else:
            continue
    return a_dictionary
