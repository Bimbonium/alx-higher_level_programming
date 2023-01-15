#!/usr/bin/python3
"""Class to define a square, with an attribute size"""


class Square:
    """Class with a size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
