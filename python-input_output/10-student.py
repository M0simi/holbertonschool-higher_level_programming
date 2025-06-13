#!/usr/bin/python3
"""
a class that have public instance attributes
and public method
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {key: getatter(self,key) fornkey in attrs if hasatter(self, key)}
        return self.__dict__
