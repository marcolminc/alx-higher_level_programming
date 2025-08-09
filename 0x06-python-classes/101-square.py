#!/usr/bin/python3

"""A module that defines a square class based on 5-square.py

This module implements a geometric square with controlled access to its size
and position attributes through property decorators, following Pyton best
practices for encapsulation and data validation.
"""


class Square:
    """A class that represents a geometric square with validation.

    The square class encapsulates a square shape with controlled access to
    its size and position attributes. This ensures these attributes always
    remain valid according to specified constraints.

    Attributes:
        __size (int): Private instance attribute storing the square side length
        __position (tuple): Private instance attribute storing the square's
        coordinates as a tuple of two positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with validation.

        Args:
            size (int, optional): The length of each side. Defaults to 0.
            position (tuple, optional): The (x, y) coordinates of the
            square's position in quadrant I. Must be a tuple of two positive
            integers. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
            of two positive integers.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Get or set square's size.

        Raises:
            TypeError: Iff value is not an integer.
            ValueError: If value is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """tuple: Get or set the square's position.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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

    def my_print(self):
        """Prints in stdout the square with the character #.
        """
        if self.size != 0:
            [print("") for i in range(0, self.position[1])]
            for j in range(self.size):
                [print(" ", end="") for j in range(0, self.position[0])]
                [print("#", end="") for k in range(0, self.size)]
                print()
        else:
            print()

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The square drawn using symbol #.
        """
        square_str = ""
        if self.size != 0:
            for i in range(0, self.position[1]):
                square_str += "" + '\n'
            for j in range(self.size):
                for k in range(0, self.position[0]):
                    square_str += " "
                for symbol in range(0, self.size):
                    square_str += "#"
                    if symbol >= self.size - 1 > j:
                        square_str += '\n'
        else:
            square_str += '\n'
        return square_str
