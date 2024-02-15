#!/usr/bin/python3
"""
Module 2-matrix_divided
a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    a function that devides all elements of a matrix.

    Args:
    matrix (list(list)): a list of list of same size of ints or floats.
    div (int of floats): divisor.
    Returns:
    new matrix of the results of division by div.
    Raises:
    TypeError: if the matrix rows are diffrent size,
               if the matrix contains a non num,
               if div is not int or float.
    ZeroDivisionError:
               if div = 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
