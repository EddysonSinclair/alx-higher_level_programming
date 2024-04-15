#!/usr/bin/python3
""" Rectangle Class"""


class Rectangle:
    """ This defiens a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """ this is the property getter for height"""
    @property
    def height(self):
        return(self.__height)

    """ this is a setter for height"""
    @height.setter
    def height(self, value):
        if (not isinstance(value, int) and value is not None):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """This is the property getter for width"""
    @property
    def width(self):
        return(self.__width)

    """ this is a setter for width"""
    @width.setter
    def width(self, value):
        if (not isinstance(value, int) and value is not None):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
