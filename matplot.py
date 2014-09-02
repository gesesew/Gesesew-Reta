from pylab import*

#from plot import*

import turtle

def draw_square(side):
     i = 0;
     while (i < 4):
         turtle.forward(side)
         turtle.left(90)
         i = i+1

     turtle.done()

def draw_rectangle (l,w):
    i=0;
    while(i<4):
        turtle.forward(l)
        turtle.left(90)
        #turtle.forward(w)
        #turtle.left(90)
        i=i+1

    turtle.done()
def draw_rhombus(l):
    i=0;
    while(i<2):
        turtle.forward(l)
        turtle.left(45)
        turtle.forward(l)
        turtle.left(135)
     #   turtle.forward(l)
     #   turtle.left(45)
        i=i+1

    turtle.done()

def draw_circle(r):
    turtle.circle(r)
    turtle.done()
def draw_semi_circle(r):
    turtle.semi_circle(r)
    turtle.done()

def draw_triangle(l):
    i=0
    while(i<3):
        turtle.forward(l)
        turtle.left(120)
        i=i+1
    turtle.done()

def draw_isosceles_trapezium(l,w,s):
   # i=0
    #while(i<1):
        turtle.forward(l)
        turtle.left(100)
        turtle.forward(w)
        turtle.left(80)
        turtle.forward(s)
        turtle.left(80)
        turtle.forward(w)
        turtle.done()

def draw_regular_hexagon(l):
    i=0
    while(i<6):
        turtle.forward(l)
        turtle.left(60)
        i=i+1
    turtle.done()
def draw_parallelogram(l,w):
    i=0
    while(i<2):
        turtle.forward(l)
        turtle.left(80)
        turtle.forward(w)
        turtle.left(100)
        i=i+1
    turtle.done()
def draw_right_angle_triangle(x,y,r):

        turtle.forward(x)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(135)
        turtle.forward(r)
        turtle.done()


if __name__== "__main__":

    #draw_square(55)
    #draw_triangle(100)
    #draw_rectangle(100,200)
    #draw_circle(100)
    draw_semi_circle(100)
    #draw_rhombus(100)
    #draw_regular_hexagon(100)
    #draw_isosceles_trapezium(123,100,90)
    #draw_right_angle_triangle(200,200,282.8)
    #draw_parallelogram(80,100)