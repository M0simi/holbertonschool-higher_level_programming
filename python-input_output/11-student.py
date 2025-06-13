#!/usr/bin/python3
"""
A class that has public instance attributes
and public methods for JSON serialization and deserialization.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of Student instance.
        If attrs is a list of strings, only include those attributes.
        Otherwise, include all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with key-value pairs from json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
