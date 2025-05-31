#!/usr/bin/python3
"""
This module defines an abstract class 'Animal' and its subclasses 'Dog' and 'Cat'.

The 'Animal' class enforces a contract that all subclasses must implement
the 'sound' method, which returns a string representing the sound the animal makes.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    All subclasses must implement the 'sound' method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by all subclasses.

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Concrete subclass representing a dog.

    Implements the 'sound' method to return 'Woof!'.
    """

    def sound(self):
        return "Woof!"


class Cat(Animal):
    """
    Concrete subclass representing a cat.

    Implements the 'sound' method to return 'Meow!'.
    """

    def sound(self):
        return "Meow!"
