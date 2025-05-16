#!/usr/bin/python3
"""
Module 2-matrix_divided
Performs matrix division with proper validation and rounding.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Matrix must be a list of lists of ints/floats.
    Each row must be the same size.
    div must be a number and not zero.
    Returns a new matrix with results rounded to 2 decimals.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

        >>> matrix_divided([[1, 3.13, 4], [56, 2, 12.34]], 2)
        [[0.5, 1.57, 2.0], [28.0, 1.0, 6.17]]

        >>> matrix_divided([[], [4, 4.5]], 2)
        [[], [2.0, 2.25]]

        >>> matrix_divided([[-3, 0, 4], [4, 54, 6.45]], 1)
        [[-3.0, 0.0, 4.0], [4.0, 54.0, 6.45]]

        >>> matrix_divided([[1, 2], [3, 4]], 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero

        >>> matrix_divided([[1, 2], [3, "a"]], 1)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided([[float('nan'), 2], [3, 4]], 2)
        [[nan, 1.0], [1.5, 2.0]]

        >>> matrix_divided([[1, 2], [3, 4]], float('nan'))
        Traceback (most recent call last):
            ...
        TypeError: div must be a number
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or div != div:  # handles NaN
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
