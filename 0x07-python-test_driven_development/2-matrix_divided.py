#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    new = []
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        mod = []
        for elements in row:
            fake = round(elements / div, 2)
            mod.append(fake)
        new.append(mod)
    return new
