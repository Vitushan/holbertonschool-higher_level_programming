#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Matrix must be a list of lists of ints/floats.
    Each row must be the same size.
    div must be a number and not zero.
    Returns a new matrix with results rounded to 2 decimals.
    """
    new_matrix = ""
    if not isinstance(matrix(list, int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix == len(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div(int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    print("{} / {} = {:2d}".format(matrix, div, new_matrix))