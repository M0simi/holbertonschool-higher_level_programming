#!/usr/bin/python3
"""a module that defines if it's inherits from spicefic class"""


def inherits_from(obj, a_class):
    """
    function that return True if obj inherites from a_class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
