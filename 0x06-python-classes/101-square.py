#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


class Rectangle:
    """Rectangle class with width and height attributes."""
    
    def __init__(self, width, height):
        """Initializes a new instance of the Rectangle class.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.
        
        Args:
            value (int): The width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.
        
        Args:
            value (int): The height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the rectangle.
        
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    
    def __init__(self, size):
        """Initializes a new instance of the Square class.
        
        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.
        
        Args:
            value (int): The size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.width, self.height)
