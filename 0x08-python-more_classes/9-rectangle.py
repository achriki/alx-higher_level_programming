#!/usr/bin/python3
"""This is a module to pass a Task"""


class Rectangle:
    """Class rectangle with following attributes
    Attributes:
        width (int): width of rect
        height (int): height of rect
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init magic method"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and returns
        the larger of the two.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns an instance with equal sides of length `size`.

        Args:
            size (int): length of sides of square, defaults to 0.

        Returns:
            new instance of class with equal sides

        """
        return cls(size, size)

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

    def __str__(self):
        """magic method"""
        if self.__width == 0 or self.__height == 0:
            return ""
        res = ""
        for i in range(0, self.__height):
            res += str(self.print_symbol) * self.__width + '\n'
        return res.rstrip()

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", "\
                + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
