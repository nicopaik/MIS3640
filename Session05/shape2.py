import turtle
import math
#SHAPE 2
shape2 = turtle.Turtle()
print (shape2)
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t,length, n)
circle (shape2, 100)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
def move (t, x, y):
    t.pu()
    t.setpos(x,y)
    t.pd() 
move (shape2, 10, 100)
arc (shape2, 50, 180)
move (shape2, 10,100)
arc (shape2, 50, 180)
move (shape2, 10, 30)
circle (shape2, 15)
move (shape2, 10, 130)
circle (shape2, 15 )