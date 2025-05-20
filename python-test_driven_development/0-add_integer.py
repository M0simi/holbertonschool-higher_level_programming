#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")


    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)


    return a + b
