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
