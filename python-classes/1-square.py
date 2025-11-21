#!/usr/bin/python3
"""
This module defines a Square class that represents a geometric square.
It includes validation to ensure that the size value is an integer and
that it is not negative.
"""


class Square:
    """
    Represents a square.

    This class defines a square with a private size attribute. The size is
    validated during instantiation to ensure that it is an integer and is
    greater than or equal to zero.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square. Must be an integer and
                greater than or equal to zero.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
