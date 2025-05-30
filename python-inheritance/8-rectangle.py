#!/usr/bin/python3
""" an empty class"""


class BaseGeometry:
    """Public instance method"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """reprecent of obj"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
