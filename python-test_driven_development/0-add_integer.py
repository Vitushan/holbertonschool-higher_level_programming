#!/usr/bin/python3
"""
Module 0-add_integer
This module provides a function `add_integer`that adds two numbers.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats, converting them to integers if necessary.

    Args:
        a (int, float): The first number.
        b (int, float): The second number, default is 98.
    Returns:
        int: The sum of a and b as integers.
    Raises:
        TypeError: If a or b is not an integer or float.
        OverflowError: If a or b is infinty.
        ValError: If a or b is NaN.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a in [float('-inf')] or b in [float('inf'), -float('inf')]:
        raise OverflowError("cannot convert float infinity to integer")
    if a != a or b != b:
        raise ValueError("cannot convert NaN to integer")
    a = int(a)
    b = int(b)
    return a + b
