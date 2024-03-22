#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    new = {x: x*2 for x in new.values()}
    return (new)
