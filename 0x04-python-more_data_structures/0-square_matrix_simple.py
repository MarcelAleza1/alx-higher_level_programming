#!/usr/bin/python3
def squre_matrix_simple(matrix=[]):
    """
    function to compare the square
    value of all integers of a matrix.
    """
    result = []
    for x in matrix:
        result.append([p ** 2 for p in x])
    return result
