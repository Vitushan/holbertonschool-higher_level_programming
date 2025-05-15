#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Matrix must be a list of lists of ints/floats.
    Each row must be the same size.
    div must be a number and not zero.
    Returns: a new matrix with results rounded to 2 decimals.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row_length = len(matrix[0])

            for row in matrix:
                if len(row) != row_length:
                    raise TypeError("Each row of the matrix must have the same size")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_matrix = []
            for row in matrix:
                new_row = []
            for value in row:
                result = round(value / div, 2)
                new_row.append(result)
            new_matrix.append(new_row)
            return new_matrix
