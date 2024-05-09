#!/usr/bin/python3
"""
This is a function that prints two arguments {first_name} and {last_name}
ARG1: This represents the first_name.
ARG2: This represents the second parameter '''last_name'''
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif not last_name:
        print("My name is {}".format(first_name))
    elif say_my_name is None:
        raise TypeError("say_my_name() missing 1 required positional"
                        "argument: 'first_name'")
    else:
        print("My name is {} {}".format(first_name, last_name))
