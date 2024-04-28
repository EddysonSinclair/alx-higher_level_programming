#!/usr/bin/python3

# this is a function to add two integers


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))