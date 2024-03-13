#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    a, b = tuple_a[:2]
    c, d = tuple_b[:2]

    sum_1 = a + c
    sum_2 = b + d
    newtup = (sum_1, sum_2)
    return (newtup)
