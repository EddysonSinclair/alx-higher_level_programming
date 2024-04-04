#!/usr/bin/python3
import sys
"""
Write a function that prints an integer.
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (False)
