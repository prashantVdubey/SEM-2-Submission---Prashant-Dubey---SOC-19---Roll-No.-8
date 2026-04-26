# shapes.py  — User-defined module
import math

def area_circle(radius):
    """Returns the area of a circle given its radius."""
    if radius < 0:
        raise ValueError('Radius cannot be negative.')
    return math.pi * radius ** 2

def area_rectangle(length, width):
    """Returns the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError('Dimensions cannot be negative.')
    return length * width

def area_triangle(base, height):
    """Returns the area of a triangle given base and height."""
    if base < 0 or height < 0:
        raise ValueError('Dimensions cannot be negative.')
    return 0.5 * base * height
