#!/usr/bin/python3
def print_last_digit(number):
    last = ""
    if number < 0:
        number = -(number)
        last = number % 10
    else:
        last = number % 10
    print("{}".format(last), end="")
    return (last)
