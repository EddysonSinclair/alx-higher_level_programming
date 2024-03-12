#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)

    for i in matrix:
        if len(i) == 0:
            print()
        for j in range(len(i)):
            print("{:d}".format(i[j]), end="\n"
                    if j == len(i) -1 else " ")
