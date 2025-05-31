#!/usr/bin/python3
"""Abstract class that have more subclass"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """The abstract class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """first subclass called Dog"""

    def sound(self):
        return "Woof!"


class Cat(Animal):
    """second subclass called Cat"""

    def sound(self):
        return "Meow!"
