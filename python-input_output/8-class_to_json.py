#!/usr/bin/python3
"""
This module defines a function that
return ictionary description with simple data structure
"""


def class_to_json(obj):
    return obj.__dict__
