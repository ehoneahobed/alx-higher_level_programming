#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """An empty class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        "initializes attributes for this class"
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if(not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if(not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__height = value
