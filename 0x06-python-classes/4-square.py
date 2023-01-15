#!/usr/bin/python3
"""Class to define a square, with an attribute size"""


class Square:
    """Class square with a size and an area"""
    def __init__(self, size=0):
        """Initialization with size constrained to the int type"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method to return the area of a square"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter to get the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
