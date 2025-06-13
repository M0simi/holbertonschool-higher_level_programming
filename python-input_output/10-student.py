#!/usr/bin/python3
"""
This module defines a class Student with public instance attributes
and methods for JSON serialization and deserialization.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If `attrs` is a list of strings, only return those attributes
        that are listed in `attrs` and exist in the object.

        Args:
            attrs (list): Optional list of attribute names.

        Returns:
            dict: Dictionary representation of selected or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
