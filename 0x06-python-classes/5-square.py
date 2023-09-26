#!/usr/bin/python3
"""This is a module to pass a Task
Here we define a class Square
"""


class Square:
    """This is an empty class
    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        """Validate if size is an integer
        It must also be superiour or qual to zero
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
