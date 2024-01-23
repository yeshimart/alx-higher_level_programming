#!/usr/bin/python3
"""Defines a square with private instance attribute and area method."""


class Square:
    """Square class with private instance attribute and area method."""
    
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
