#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def pascal_triangle(n):
    """
    pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
