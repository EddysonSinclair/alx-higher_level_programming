#!/usr/bin/python3
def weight_average(my_list=[]):
    pdt_score = 0
    weight = 0
    if my_list is None or len(my_list) == 0:
        return (0)

    for element in my_list:
        pdt_score += element[0] * element[1]
        weight += element[1]
        if weight == 0:
            return (0)
    return (pdt_score/weight)
