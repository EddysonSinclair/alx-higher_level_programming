#!/usr/bin/python3
def weight_average(my_list=[]):
    pdt_score = 0
    weight = 0
    if my_list is None:
        return (0)

    for element in my_list:
        pdt_score += element[0] * element[1]
        weight += element[1]
    return (pdt_score/weight)
