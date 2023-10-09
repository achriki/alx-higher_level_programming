#!/usr/bin/python3
"""This a module's comment"""


def is_same_class(obj, a_class):
    """Return the validity of an object class
    Args:
        obj: object class
        a_class: class name
    """
    verf = False
    if type(obj) == a_class:
        verf = True
    return verf
