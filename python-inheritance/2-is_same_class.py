#!/usr/bin/python3
"""Check if object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """function that check if a class is same type or not"""
    return type(obj) is a_class
