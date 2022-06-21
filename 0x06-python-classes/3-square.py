#!/usr/bin/python3
"""Define a Square class."""

class Square:
    """Class to represent  square

    Args:
        size (int): square size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

    def area(self):
        """Return area of the square."""
        return (self.___size * self.__size)
