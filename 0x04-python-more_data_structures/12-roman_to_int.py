#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if not (isinstance(roman_string, str)):
        return (0)
    total = 0
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    prev = roman_dict[roman_string[0]]
    for i in range(1, len(roman_string)):
        current = roman_dict[roman_string[i]]
        if prev < current:
            total -= prev
        else:
            total += prev
        prev = current
    total += prev
    return (total)
