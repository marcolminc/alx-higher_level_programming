#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res_matrix = [[col**2 for col in row] for row in matrix]
    return res_matrix
