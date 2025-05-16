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
    Adds two integers or floats.

    Both arguments are casted to integers if they are floats.
    Raises a TypeError if the arguments are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
