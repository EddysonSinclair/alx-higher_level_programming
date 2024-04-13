#!/usr/bin/python3
""" class Square"""


class Square:
    """Defining a Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """ Getter function for position"""
    @property
    def position(self):
        return (self.__position)

    """setter function for position"""
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
