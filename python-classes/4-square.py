#!/usr/bin/python3
"""
This module defines a Square class that represents a geometric square.
It allows access and updating of the private size attribute, computes
the area, and prints the square using the '#' character.
"""


class Square:
    """
    Represents a square.

    This class defines a square with a private size attribute. The size is
    validated during instantiation and assignment. The square can compute
    its area and print itself using the '#' character.
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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square. Must be an integer
                and greater than or equal to zero.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the '#' character.

        Prints lines of '#' equal to the size of the square. If size is
        0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
