#!/usr/bin/python3
"""
pascal triangle
"""

def pascal_triangle(n):
    """
    every line start by 1 and every elements inside 1 their sum is greater
    """
    def pascal_triangle(n):
        """
        return a list of the list representing pascal triangle
        """
        if n <= 0:
            return []
