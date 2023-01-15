#!/usr/bin/python3
"""Module documentation test keeps failing, so trying a new line"""
"""Class to define a square, with an attribute size"""


class Square:
    """Class square with a size and an area"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization with size constrained to the int type"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or type(position[1]) is not int\
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """attribute getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Attribute setter for position tuple"""
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method to print out the square, represented by #"""
        if self.size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
                printer = '#' * self.__size
                margin = " " * self.__position[0]
                for x in range(self.__size):
                    print(margin, printer, sep="")
