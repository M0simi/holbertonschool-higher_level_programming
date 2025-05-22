#!/usr/bin/python3
"""THis class is with private and public instance"""


class Square:
    """class eith private and public inistance"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= o")
        else:
            self.__size = value

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for x in range(self.size):
                    print("#", end="")
                print()
