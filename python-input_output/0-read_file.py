#!/usr/bin/python3
"""
This module defines a function that reads a text file
and prints its content to stdout.
"""


def read_file(filename=""):
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
