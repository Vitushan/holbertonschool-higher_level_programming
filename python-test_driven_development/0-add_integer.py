#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers (or floats) and returns the result as an integer.
    
    Args:
    a: first number, must be an integer or a float.
    b: second number, must be an integer or a float. Defaults to 98.
    
    Raises:
    TypeError: if a or b is not an integer or float.
    
    Returns:
    int: the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
