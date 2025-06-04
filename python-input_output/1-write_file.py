#!/usr/bin/python3
"""
This module defines a function that writes text to a file and returns character count.
"""


def write_file(filename="", text=""):
    """function that write into a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
