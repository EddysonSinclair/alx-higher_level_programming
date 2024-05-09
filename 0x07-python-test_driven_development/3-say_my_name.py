#!/usr/bin/python3
"""
This is a function that prints two arguments {first_name} and {last_name}
"""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
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
