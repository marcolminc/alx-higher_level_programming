#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix
    Args:
        matrix - the matrix
    Return:
        new (squared) matrix)
    """
    new_matrix = []
    if matrix:
        for row in matrix:
            new_matrix.append([num ** 2 for num in row])
    return new_matrix
