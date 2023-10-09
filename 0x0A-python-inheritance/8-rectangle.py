#!/usr/bin/python3
"""This a module's comment"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inher class"""

    def __init__(self, width, height):
        """init function"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
