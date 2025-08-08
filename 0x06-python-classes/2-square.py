#!/usr/bin/python3

"""A module that defines a square class based on 1-square.py

This class initializes size with optional value which must be an integer
greater than zero.
"""


class Square:
    """A class that represents a geometric square.

    It initializes size with an optional value which must be an integer
    greater than zero.
    Attributes:
        __size: The length of each side of the square. This attribute is
        private and should not be accessed directly
    """
    def __init__(self, size=0):
        """Initializes a new Square instance with the given size.

        The initialization method sets up the fundamental property of the
        square shape. The size value is stored in a private attribute to
        enforce encapsulation. Size must be an integer greater than zero

        Args:
            size: The length of each side of the square. Must be positive
            integral value.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
