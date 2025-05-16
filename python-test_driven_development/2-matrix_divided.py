#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    >>> matrix_divided([[1, 2], [3, 4]], 1)
    [[1.0, 2.0], [3.0, 4.0]]

    >>> matrix_divided([[2, 4], [6, 8]], 2)
    [[1.0, 2.0], [3.0, 4.0]]

    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    >>> matrix_divided([[1, 2], [3, "a"]], 1)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list)
                for row in matrix) or
        not all(isinstance(num, (int, float))
                for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
