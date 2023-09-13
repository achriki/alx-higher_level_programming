#!/usr/bin/python3
def best_score(a_dictionary):
    key_max = ""
    if a_dictionary is not None and a_dictionary != {}:
        key_max = max(a_dictionary)
    else:
        key_max = None
    return key_max
