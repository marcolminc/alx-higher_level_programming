#!/usr/bin/python3

"""The magic class."""


class MagicClass:
    """The magic class as per provided pycode."""

    def __init__(self, radius=0):
        """Initializes MagicClass's instance with validation.

        Args:
            radius (int, float): the radius of the (shape).
            It must be a number.

        Raises:
            TypeError: If radius is not a number.
        """
        if not isinstance(radius, int):
            if not isinstance(radius, float):
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """computes area of the shape.

        Returns:
            (int, float): The area of the shape.
        """
        from math import pi
        return (self.__radius ** 2) * pi

    def circumference(self):
        """computes the circumference of the shape (circle).

        Returns:
            (int, float): The circumference of the circle.
        """
        from math import pi
        return self.__radius * 2 * pi
