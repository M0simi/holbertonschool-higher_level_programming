#!/usr/bin/python3
"""
This module defines a class MyList that inherits from Python's
built-in list class
and provides a method to print the list in a sorted (ascending) order.
"""


class MyList(list):
    """The chiled class"""

    def print_sorted(self):
        """
        Prints the list in ascending sorted
        order without modifying the original list.
        """
        print(sorted(self))
