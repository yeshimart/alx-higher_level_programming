#!/usr/bin/python3
"""Defines a square with private instance attribute."""


class Square:
    """Square class with private instance attribute."""
    
    def __init__(self, size=0):
        """Initializes a new instance of the Square class.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
