#!/usr/bin/python3
"Define a class Square"


class Square:
    """Class Square that defines a square"""i
    def __init__(self, size=0):
        """Initializes attribute size """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """Calculate area of square"""
            return (self.__size * self.__size)
