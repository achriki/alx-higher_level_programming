#!/usr/bin/python3
def best_score(a_dictionary):
    key_max = ""
    if not a_dictionary or a_dictionary == {}:
        key_max = None
    else:
        key_max = max(a_dictionary)
    return key_max
