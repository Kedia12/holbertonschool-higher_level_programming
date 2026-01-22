#!/usr/bin/python3
"""2-matrix_divided module.

This module provides matrix_divided(matrix, div).
It divides all elements of a matrix by div and rounds to 2 decimals.
No modules are imported.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Returns a new matrix with each element divided by div (rounded to 2 decimals).
    """
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) for row in matrix) or
            any(row == [] for row in matrix) or
            any(any(type(item) not in (int, float) for item in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
