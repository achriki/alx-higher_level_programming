#!/usr/bin/python3
"""class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Derived class"""

    def __init__(self,size):
        """init method"""

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate area of width and height"""
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}".format(__class__.__name__,
                                    self.__size,self.__size)
