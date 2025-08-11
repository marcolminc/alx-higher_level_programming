#!/usr/bin/python3

"""A module that defines a Square class with size validation and comparison.

This module implements a geometric square with controlled access to its size
attribute through property decorators, following Python best practices.
The class includes comparison methods based on square areas.
"""


class Square:
    """A class that represents a geometric square with size validation.

    The square class encapsulates a square shape with controlled access to
    its size attribute through property decorators. This ensures the size
    always remains a valid positive integer.
    The class implements comparison operations based on the squares' areas.

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
        """int: Gets or sets the square's size with validation.

        The getter returns the current size of the square.
        The setter validates and sets the size, ensuring it remains a
        non-negative integer.

        Returns:
            int: The current size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        Example:
            >>> square = Square(5)
            >>> square.size
            5
        """
        return self.__size

    @size.setter
    def size(self, value):
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

    def __eq__(self, other):
        """Compares if two squares have equal areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """Compares if this square's area is less than another's.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if this square's area is less than another's, False
            otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compares if this square's area is less than or equal to another's.

        Args:
            other (Square): The other square to compare with this one

        Returns:
            bool: True if this square's area is less than or equal to another's
            , False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares if this square's area is greater than another's.

        Args:
            other (Square): The other square to compare with this one

        Returns:
            bool: True if this square's area is greater than another's,
            False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares if this square's area is greater than or equal to another's

        Args:
            other (Square): The other square to compare with this one

        Returns:
            bool: True if this square's area is greater than or equal to
            another's, False otherwise.
        """
        return self.area() >= other.area()
