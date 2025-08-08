#!/usr/bin/python3

"""A module that defines a square class based on 1-square.py

This module implements a geometric square with controlled access to its size
attribute through getter and setter methods, following Python best practices.
"""


class Square:
    """A class that represents a geometric square with size validation.

    The square class encapsulates a square shape with controlled access to
    its size attribute through property decorators. This ensures the size
    always remains a valid positive integer.

    Attributes:
        __size: Private instance attribute storing the square side length.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with size validation.

        Args:
            size (int, optional): The length of each side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for the square's size.

        Provides controlled read access to the private __sie attribute.

        Returns:
            int: The current size of the square's sides.

        Example:
            >>> square = Square(5)
            >>> square.size
            5
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the square's size with validation.
        Provides controlled write access to the private __size attribute,
        ensuring the size remains a valid positive integer.

        Args:
            value (int): The new size for the square's sides.

        Raises:
            TypeError: Iff value is not an integer.
            ValueError: If value is less than 0.

        Example:
            >>> square = Square()
            >>> square.size = 10
            >>> square.size
            10
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square (size²)

        Example:
            >>> square = Square(4)
            >>> square.area()
            16
        """
        return self.__size ** 2
