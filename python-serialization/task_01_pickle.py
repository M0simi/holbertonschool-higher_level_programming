#!/usr/bin/python3
"""
Module: task_01_pickle

This module defines a custom class `CustomObject` with methods to
serialize and deserialize using the pickle module.
"""

import pickle


class CustomObject:
    """
    A class representing a custom object with name, age,
    and is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the object in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Args:
            filename (str): The filename where the object will be saved.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Args:
            filename (str): The filename to read the object from.

        Returns:
            CustomObject or None: The deserialized object, or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None
