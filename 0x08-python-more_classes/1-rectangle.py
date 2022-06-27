#!/usr/bin/python3
"""
    Single class module
"""


class Rectangle:
    """Defines a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of class"""
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be an integer")
        if width < 0:
            raise ValueError("width must be an integer")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """returns value of width"""
            return self.__width

        @property
        def height(self):
            """returns vakue of height"""
            return self.__height

        @width.setter
        def width(self, value):
            """set a new value to width"""
            if not isinstance(value, (int, float)):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """set a new value to height"""
            if not isinstance(value, (int, float)):
                raise TypeError("height must be an integer")
            if value < 0:
                raise valueError("height must be >= 0")
            self.__height = value
