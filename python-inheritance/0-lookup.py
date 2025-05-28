#!/usr/bin/python3
"""
This module provides a function to return the list of available
attributes and methods of a given object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the object's attributes and methods.
    """
    return dir(obj)
