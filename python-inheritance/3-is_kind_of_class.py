#!/usr/bin/python3
"""Check if object is instance or inherits from a class"""


def is_kind_of_class(obj, a_class):
    """function that dfined if it's a kind of class

    Args: obj, A_class

    return True or False
    """
    return isinstance(obj, a_class)
