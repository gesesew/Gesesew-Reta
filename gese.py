from math import sqrt
from numbers import Number
def square_perimeter(side:Number)->Number:
    """
     calculate perimeter of square from side length.
    @parmside:the side length
    @return:the area (units as sidelength)
      square_perimeter(4)
    """
    return 4*side
print (square_perimeter(7))
def square_area(side):
    """
    calculate the area of a square from side length.
    :param side: the side length
    :return:the area (units^2 from side)
    square_area(*)
    28
    """
    return side*side
print (square_area(7))
if __name__=="__main__":
    sampleSide = 7
    print("area:",
          square_area(7),
          "perimeter:",
          square_perimeter(7))
def area_hexagon(s):
    """
    cal
    :param s: side length
    :return:area
    """
    area=(3*(sqrt(3)*s**2)/2)
    return area
print (area_hexagon(4))