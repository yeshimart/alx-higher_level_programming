#!/usr/bin/python3
"""Defines a square with private instance attribute, area method, and size getter and setter."""


class Square:
    """Square class with private instance attribute, area method, and size getter and setter."""
    
    def __init__(self, size=0):
        """Initializes a new instance of the Square class.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.
        
        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
