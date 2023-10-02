#!/usr/bin/python3
"""This is a module to pass a Task"""


class Rectangle:
    """Class rectangle with following attributes
    Attributes:
        width (int): width of rect
        height (int): height of rect
    """
    def __init__(self, width=0, height=0):
        """init magic method"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter Method"""
        return self.__height

    @property
    def width(self):
        """Getter Method"""
        return self.__width

    @height.setter
    def height(self, value):
        """Setter Method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter Method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    def area(self):
        """method that returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """method that returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
