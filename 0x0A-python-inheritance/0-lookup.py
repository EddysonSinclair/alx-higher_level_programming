#!/usr/bin/python3
"""
Return a list of available attributes and methods of an object.

Args:
    obj: Any Python object.
    
Returns:
    list: A list containing the names of attributes and methods of the object.
"""


def lookup(obj):
    if obj is None:
        return None
    if not hasattr(obj, '__dir__'):
        return None
    return (dir(obj))
