#!/usr/bin/python3
"""
This module defines a function that append text to a file
and returns character count.
"""


def append_write(filename="", text=""):
    """function that append to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    return count
