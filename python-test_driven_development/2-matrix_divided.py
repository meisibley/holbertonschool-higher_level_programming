#!/usr/bin/python3
"""using argument div divideds all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of int or float"""

    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(err1)
    for i in range(len(matrix)):
        if type(matrix[i]) != list or len(matrix[i]) == 0:
            raise TypeError(err1)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(err1)
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError(err2)
    if type(div) not in [int, float]:
        raise TypeError(err3)
    if div == 0:
        raise ZeroDivisionError(err4)
    newmatrix = [list(map(lambda cc: round(cc / div, 2), rc)) for rc in matrix]
    return newmatrix
