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
    """
    if not isinstance(a, (int, float)):
        raise TypeError ("must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
