#!/usr/bin/python3
# 0-square.py by Ehoneah Obed
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer or if position isn't
                       a tuple of 2 positive integers
            ValueError: if size is less than zero
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves size of square"""

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
        """Get position attribute of square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set values for position of the square"""

        err_msg = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple) and len(value) != 2):
            raise TypeError(err_msg)
        for num in value:
            if (not isinstance(num, int) or num < 0):
                raise TypeError(err_msg)

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
