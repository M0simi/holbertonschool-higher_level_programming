#!/usr/bin/python3
"""THis class is with private and public instance"""


class Square:
    """class with private and public inistance"""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        # when creating make sure of position
        if (not isinstance(position, tuple)
            or len(position) != 2
                or not all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        """public instance method that returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print the square with '#' using position for spacing"""
        if self.size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            """print empty line based on position[1]"""
            print()

        for _ in range(self.__size):
            """print each line of square"""
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
            or len(value) != 2
                or not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
