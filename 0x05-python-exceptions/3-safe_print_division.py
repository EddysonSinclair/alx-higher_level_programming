#!/usr/bin/python3
# 3-safe_print_division.py


def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return(result)
