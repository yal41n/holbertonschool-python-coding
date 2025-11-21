#!/usr/bin/python3
"""
This module defines a Square class that represents a geometric square.
It includes size validation to ensure the value is an integer and non-negative.
"""


class Square:
    """
    Represents a square.

    This class defines a square with a private size attribute. The size must be
    a valid integer greater than or equal to zero. Validation is performed during
    instantiation to ensure correctness of the stored value.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
