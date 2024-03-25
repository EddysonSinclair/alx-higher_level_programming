#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    max_value = 0
    if a_dictionary == None or not a_dictionary:
        return (None)
    for k, v in a_dictionary.items():
        if v > max_value:
            max_value = v
            best_key = k
    return (best_key)
