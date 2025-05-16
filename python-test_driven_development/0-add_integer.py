#!/usr/bin/python3
"""
This module provides a function to add two integers.

It ensures that both arguments are integers or floats,
casts floats to integers before addition,
and raises appropriate errors for invalid inputs.

The function is designed for educational purposes
following the TDD (Test Driven Development) approach.
"""


def add_integer(a, b=98):
    """
    args: a and b must be integers or floats,
    raise: otherwise raise a TypeError exception with
    the message a must be an integer
    or b must be an integer
    a and b must be first casted to integers if they are float
    Returns: an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
