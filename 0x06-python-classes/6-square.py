#!/usr/bin/python3
"""Class to define a square, with an attribute size"""


class Square:
    """Class square with a size and an area"""
    def __init__(self, size=1, position=(0, 0)):
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
            def position(self, value)
            """Attribute setter for position tuple"""
            if type(value) is tuple and len(value) = 2\
               and type(value[0]) is int and type(value[1]) is int\
               and value[0] >= 0 and value[1] >= 0:
                self.__position = value
                return
            raise TypeError("position must be a tuple of 2 positive integers")

        def my_print(self):
            """Method to print out the square, represented by #"""
            if self.size == 0:
                print()
            else:
                for x in range(self.__position[1]):
                    print()
                    printer = '#' * self.__size
                    margin = " " * self.position[0]
                    for x in range(self.__size):
                        print(margin, printer, sep="")
