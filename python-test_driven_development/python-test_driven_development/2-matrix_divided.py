#!/usr/bin/python3
"""
Module 0-matrix_divided
This module provides a function `matrix_divided` that divides all elements
of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds to 2 decimals.

    Args:
        matrix (list of list of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of list of float: A new matrix with each element divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If all rows in the matrix are not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(item, (int, float)) for item in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
