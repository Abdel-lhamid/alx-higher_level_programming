#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        sqr_matrix = []
        for i in matrix:
            sqr_matrix.append(list(map(lambda x: x**2, i)))
        return sqr_matrix
