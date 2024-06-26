#!/usr/bin/python3
""" class Square"""


class Square:
    """Defining a Square"""
    def __init__(self, size=0):
        self.__size = size

    """ Getter function """
    @property
    def size(self):
        return (self.__size)

    """ setter function """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
