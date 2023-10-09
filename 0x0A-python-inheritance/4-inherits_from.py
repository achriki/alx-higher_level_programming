#!/usr/bin/python3
"""This a module's comment"""


def inherits_from(obj, a_class):
    """Return the validity of an object class
    Args:
        obj: object class
        a_class: class name
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
