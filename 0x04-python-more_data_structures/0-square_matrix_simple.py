#!/usr/bin/python3
def squre_matrix_simple(matrix=[]):
    """
    function to compare the square
    value of all integers of a matrix.
    """
    mat = []
    for column in matrix:
        result = list(map(lambda val: val**2, column))
        mat.append(result)
    return mat
