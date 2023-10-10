#!/usr/bin/python3
"""
5-save_to_json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file -  writes an Object to a text file,
                        using a JSON representation:
    Args:
        my_obj:
        filename:
    Return:
    """
    json_rep = json.dumps(my_obj)
    with open(filename, "w") as f:
        return f.write(json_rep)
