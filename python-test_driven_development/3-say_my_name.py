#!/usr/bin/python3
"""This module defines a function that prints a person's full name."""


def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first name> <last name>

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional).

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
