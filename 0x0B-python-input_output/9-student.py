#!/usr/bin/python3
"""Module for Class Student"""


class Student:
    """This is the Student Class"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation of Student.
        """
        return self.__dict__
