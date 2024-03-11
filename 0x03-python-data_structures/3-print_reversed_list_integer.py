#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    else:
        num = len(my_list)
        a = -1
        for i in range (num):
            print("{}".format(my_list[a]))
            a += -1
