import turtle
import math
#SHAPE 1
shape1 = turtle.Turtle()
print (shape1)
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t,length, n)
circle (shape1, 100)
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
shape1.left (60)
arc (shape1, 100, 120)
shape1.left (120)
arc (shape1, 100, 120)
shape1.left (120)
arc (shape1, 100, 120)
move (shape1,0,200)
shape1.right(60)
arc (shape1, 100, 120)
shape1.left (120)
arc (shape1, 100, 120)
shape1.left (120)
arc (shape1, 100, 120)
turtle.mainloop()