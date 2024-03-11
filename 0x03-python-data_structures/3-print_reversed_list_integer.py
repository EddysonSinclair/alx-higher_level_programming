#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
        return (my_list)
    else:
        new = my_list[::-1]
        for i in range (len(new)):
            print("{:d}".format(new[i]))
