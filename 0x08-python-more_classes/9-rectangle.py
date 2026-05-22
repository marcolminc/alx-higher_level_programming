#!/usr/bin/python3
"""Define a geometric shape - Retcangle.

This module defines a class representing a geometric shape - rectangle.
"""


class Rectangle:
    """Represent a geometric shape - Rectangle.

    Attributes:
    number_of_instances(int): Number of instances of the Rectangle class.
    print_symbol(any): A symbol for printing the rectangle
    (a public class attribute).
    __width(int): How long the rectangle is (a private attribute).
    __height(int): How high the rectangle is (a private attribute).

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize rectangle properties and increment instances."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determine the bigger rectangle between given two ones.

        Returns:
            Rectangle: The bigger rectangle between rect_1 and rect_2.

        Raises:
            TypeError: If rect_1 or rec_2 is not a Rectangle instance.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square by Rectangle.

        Args:
            size(int): size of the square to create.

        Returns:
            Rectangle: The rectangle with width = height - square.

        """
        return cls(size, size)

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
                row = str(self.print_symbol) * self.width
                res.append(row)

        return '\n'.join(res) if len(res) else ''

    def __repr__(self):
        """Represent the rectangle as a parsable string.

        Returns:
            str: The parsable string representation of the rectangle.

        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Recognize destruction of the rectangle and decrement instances."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
