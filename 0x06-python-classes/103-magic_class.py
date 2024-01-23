#!/usr/bin/python3
"""Defines a MagicClass class."""


import math


class MagicClass:
    """MagicClass class that mimics a bytecode from a given class."""
    
    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass class.
        
        Args:
            radius (float): The radius of the circle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """Calculates the area of the circle.
        
        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle.
        
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
