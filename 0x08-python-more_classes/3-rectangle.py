#!/usr/bin/python3
"""Define a geometric shape - Retcangle.

This module defines a class representing a geometric shape - rectangle.
"""


class Rectangle:
    """Represent a geometric shape - Rectangle.

    Attributes:
    __width(int): How long the rectangle is (a private attribute).
    __height(int): How high the rectangle is (a private attribute).

    """

    def __init__(self, width=0, height=0):
        """Initialize rectangle properties."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Give value of width of the rectangle.

        Returns:
            int: Width of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set value of width of the rectangle.

        Args:
            value(int): New integer value for width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Give value of height of the rectangle.

        Returns:
            int: height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set value of height of the rectangle.

        Args:
            value(int): New integer value for height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculate area of the rectangle.

        Returns:
            int: width times height.

        """
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of the rectangle.

        Returns:
            int: Twice the sum of height and width of the rectangle.
            If height or width is zero, zero is returned.

        """
        if self.height and self.width:
            return 2 * (self.height + self.width)
        return 0

    def __str__(self):
        """Represent the rectangle as an output string.

        Returns:
            str: String representation of rectangle printing to stdout.

        """
        res = []
        if (self.width and self.height):
            for _ in range(self.height):
                row = '#' * self.width
                res.append(row)

        return '\n'.join(res) if len(res) else ''
