#1 1111111111111111111111111111111111111111111111111111111111111111111111111

# Assignment Submitted by: Gesesew Reta Habtie

from math import sqrt
from numpy import *
from numbers import Number

def rectangle_perimeter(side:Number)->Number:
    """
    calculate the perimeter of rectangle from side length.
    :param side: the side length
    :return:the area (unitas side length)
    """
    return 4*side
print (rectangle_perimeter(4))

#2 22222222222222222222222222222222222222222222222222222222222222222222222222222222222

def rectangle_area(l,w):
    """
    calculate the area of rectangle from the it's side length and width
    :param l: the side length
    :param w: the width
    :return:the area
    """
    rectangle_area=l*w
    return rectangle_area
print (rectangle_area(4,5))

#3 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

def trapezium_area(b1,b2,h):
    """
    calculate the area of trapezium from the b1=4,b2=6 and h=5.
    :param b1:the smallest base of trapezium
    :param b2:the longest base of trapezium
    :param h:the distance from base1 to base2
    :return:the area of trapezium
    """
    trapezium_area=((b1+b2)*h)/2
    return trapezium_area
print (trapezium_area(4,6,5))

#4 444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

def cube_volume (l):
    """
    calculate the volume of cube with side length.
    :param l: side length of cube let: l= 4cm
    :return:the volume of cube
    """
    cube_volume=l**3
    return cube_volume
print (cube_volume(4))

#5 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555

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

#6 6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666

def cylinder_volume(r, h):
    """
    calculate the volume of a cylinder with height 50cm and radius 20cm.(use pi=3.14)
    :param r: the radius of the cylinder
    :param h: the height of the cylinder
    :return:the volume of a cylinder
    """
    cylinder_volume=(pi*r**2)*h
    return cylinder_volume
print(cylinder_volume(20,50))

#7 777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777

def circle_area(r):
    """
    determine the area of the circle with radius 10cm.
    :param r: the radius of a given circle
    :return:the area of the given circle
    """
    circle_area=pi*r**2
    return circle_area
print(circle_area(10))

#8 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

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

#9 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

def perimeter_regular_hexagon(side:Number)->Number:
    """
    calculate the perimeter of regular hexagon with side 3cm.
    :param side:the length of each sides
    :return:the perimeter of the given hexagon
    """
    return 6*side
print(perimeter_regular_hexagon(3))

#10 101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010

def cuboid_volume(l,w,h):
    """
    calculate the volume of cuboid, with l=10cm, w=70cm and h=100cm.
    :param l: length of cuboid
    :param w: width of cuboid
    :param h: height of cuboid
    :return:the volume of cuboid
    """
    volume=l*w*h
    return volume
print (cuboid_volume(10,70,100))

#11 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def volume_sphere(r: Number)->Number:
    """
    calculate the volume of sphere of radius 4cm.

    @param r: the radius of the given sphere.
    @return: the volume of the given sphere.
    """
    volume = (4*pi*r**3)/3
    return volume

print(volume_sphere(4))

#12 12121212121212121212121212121212121212121212121212122121212121212121212121212121212121212121212

def area_regular_hexagon(s):
    """
    calculate the area of given regular hexagon with side length 4cm.
    :param s: length of each side of the given hexagon
    :return:area of the given hexagon.
    """
    area=(3*sqrt(3)*s**2)/2
    return area
print (area_regular_hexagon(4))

#13 1313131313131313131313131313131313131313131313133131313131313131313131313131313131313131313131

def cylinder_area(r,h):
    """
    calculate the area of a cylinder, which has 5cm radius and 20cm height.
    :param r: radius of a cylinder
    :param h: height of a cylinder
    :return:area of a cylinder
    """
    area= 2*pi*r**2 + 2*pi*r*h
    return area
print (cylinder_area(5,20))

#end end end end end




