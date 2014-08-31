from numpy import *
from numbers import Number
def rectangle_perimeter(side:Number)->Number:
    """
    calculate the perimeter of rectangel from side length.
    :param side: the side length
    :return:the area (unitas side length)
    """
    return 4*side
print (rectangle_perimeter(4))


def rectangle_area(length, width):
    """
    calculate the area of rectangle from the area side length and width
    :param length: the side length and width
    :return:the area as side length and width
    """
    return length*width
print (rectangle_area(4,5))
def circle_area(r):
    """
    determine the area of the circle with radius 10cm
    :param r: the radius of a given circle
    :return:the area of the given circle
    """
    area=pi*r**2
    return area
print(circle_area(10))

