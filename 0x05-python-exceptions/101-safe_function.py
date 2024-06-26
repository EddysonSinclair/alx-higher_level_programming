#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a = fct(*args)
        return (a)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (None)
