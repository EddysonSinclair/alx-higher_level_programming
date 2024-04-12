#!/usr/bin/python3
""" class Square"""


class Square:
    """Defining a Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """ Getter function for position"""
    @property
    def position(self):
        return (self.__position)

    """setter function for position"""
    @position.setter
    def position(self, value):
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        if self.__size != 0:
            print()
        if self.position[1] > 0:
            print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print("_" * self.position[0], end="")
            print("#" * self.size)
