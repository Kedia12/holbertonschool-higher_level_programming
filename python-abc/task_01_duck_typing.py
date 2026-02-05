#!/usr/bin/python3
"""
Module defining an abstract base class Shape with abstract methods area
and perimeter.
It also includes Circle and Rectangle classes that implement these methods,
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes with abstract methods area and perimeter.
    """
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape and implements area and
    perimeter.
    """
    def __init__(self, radius):
        """
        Initialize the circle with a radius.
        args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        args:
            radius (float): The radius of the circle.
        returns:
            float: The area of the circle.
        """
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter of the circle.
        args:
            radius (float): The radius of the circle.
        returns:
            float: The perimeter of the circle.
        """
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape and implements area and
    perimeter.
    """
    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of the given shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
