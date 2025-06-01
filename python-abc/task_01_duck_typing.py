#!/usr/bin/python3
"""
This module defines an abstract class 'Shape' and its concrete
subclasses 'Circle' and 'Rectangle'. It also provides a utility
function 'shape_info' that demonstrates duck typing by printing
shape information.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Methods:
        area(): Returns the area of the shape.
        perimeter(): Returns the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.

        Returns:
            float: The area value.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.

        Returns:
            float: The perimeter value.
        """
        pass


class Circle(Shape):
    """
    Circle shape class inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.

        Returns:
            float: Area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.

        Returns:
            float: Perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with given width and height.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.

        Returns:
            float: Area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        Returns:
            float: Perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape object.

    This function uses duck typing to work with any object that
    implements area() and perimeter() methods.

    Args:
        shape (object): Any object with area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
