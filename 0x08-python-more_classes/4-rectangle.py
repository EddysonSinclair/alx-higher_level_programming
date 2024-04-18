#!/usr/bin/python3
""" Rectangle Class"""


class Rectangle:
    """ This defines a rectangle"""

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Get/set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ function to calc area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ function to calc perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        rec = ""
        for row in range(0, self.__height):
            for column in range(0, self.__width):
                rec += '#'
            if row != self.__height - 1:
                rec += '\n'
        return rec

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")
