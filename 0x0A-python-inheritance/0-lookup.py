#!/usr/bin/python3
"""This a module's comment"""


def lookup(obj):
    """Return a list of attributes of a class
    Args:
        obj: object class
    """
    return list(i for i in dir(obj))
