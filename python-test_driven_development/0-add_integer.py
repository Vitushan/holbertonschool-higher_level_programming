#!/usr/bin/python3
"""
Module 0-add_integer
This module provides the function `add_integer` that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, returning an integer result.

    Args:
        a (int/float): The first number.
        b (int/float): The second number (default is 98).

    Returns:
        int: The result of adding a and b as integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
