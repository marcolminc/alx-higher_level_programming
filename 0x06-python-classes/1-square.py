#!/usr/bin/python3

"""A module that defines a Square class.

This module contains the implementation of a basic geometric shape, square.
"""


class Square:
    """A class that represents a geometric square.

    Attributes:
        __size: The length of each side of the square. This attribute is
        private and should not be accessed directly
    """
    def __init__(self, size):
        """Initializes a new Square instance with the given size.

        The initialization method sets up the fundamental property of the
        square shape. The size value is stored in a private attribute to
        enforce encapsulation.

        Args:
            size: The length of each side of the square. Must be positive
            integral value.
        """
        self.__size = size
