from numpy import *
from numbers import Number
def rectangle_perimeter(side:Number)->Number:
    """
    calculate the erimeter of rectangel from side length.
    :param side: the side length
    :return:the area (unitas side length)
    """
    return 4*side
print (rectangle_perimeter(4))
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def rectangle_area(length,width):
    """
    calculate the area of rectangle from the area side length and width
    :param length: the side length and width
    :return:the area as side length and width
    """
    return length*width
print (rectangle_area(4,5))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def trapezium_area(b1,b2,h):
    """
    calculate the area of trapezium from the base1,base2 and height.
    :param b1:the smallest base of trapezium
    :param b2:the longest base of trapezium
    :param h:the distance from base1 to base2
    :return:the area of trapezium
    """
    trapezium_area=((b1+b2)*h)/2
    return trapezium_area
print (trapezium_area(4,6,5))
#=============================================================================================================
def cube_volume (l):
    """
    calculate the volume of cube with side length.
    :param l: side length of cube let: l= 4cm
    :return:the volume of cube
    """
    cube_volume=(l**2)*l
    return cube_volume
print (cube_volume(4))
#==============================================================================================================
def cone_volume (h,r):
    """
    calculate the volume of the cube from the radius of the base and height.
    :param h: the perpendicular distance from base to tip of the cone =5cm
    :param r: the radius of the base which is a circle=4cm
    :return:the volume of the cube
    """
    cone_Volume=(pi*r**2*h)/3
    return cone_Volume
print (cone_volume(5,4))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def cylinder_volume(radius, height):
    """
    calculate the volume of a cylinder with height 50cm and radius 20cm.(use pi=3.14)
    :param radius: the radius of the cylinder
    :param height: the height pf the cylinder
    :return:the volume of a cylinder
    """
    return 3.14*radius*radius*height
print(cylinder_volume(20,50))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def circle_area(r):
    """
    determine the area of the circle with radius 10cm
    :param r: the radius of a given circle
    :return:the area of the given circle
    """
    Circle_area=pi*r**2
    return circle_area
print(circle_area(10))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def isosceles_triangle_area(b,h):
    """
    determine the area of isosceles triangle whose sides long 5cm, 5cm and 6cm, when the vertical distance from the
    longest side to the vertex of the equal sides is 4cm.
    :param h:the vertical distance from the base to the opposite vertex
    :parm b:the base of triangle
    :return:the area of i.triangle
    """
    area=(b*h)/2
    return area
print (isosceles_triangle_area(6,4))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def perimeter_regular_hexagon(side:Number)->Number:
    """
    calculate the perimeter of regular hexagon with side 3cm.
    :param side:the length of each sides
    :return:the perimeter of the given hexagon
    """
    return 6*side
print(perimeter_regular_hexagon(3))
#==============================================================================================

def volume_sphere(r: Number)->Number:
    """
    calculate the volume of sphere of radius 4cm.

    @param r: the radius of the given sphere.
    @return: the volume of the given sphere.
    """
    volume = (4*pi*r**3)/3
    return volume

print(volume_sphere(4))
#================================================






