#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    new = {x: new[x] * 2 for x in new}
    return (new)
