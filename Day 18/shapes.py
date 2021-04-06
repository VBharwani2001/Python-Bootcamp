from turtle import *
from random import *
t = Turtle()
screen = Screen()
screen.colormode(255)
j = 0
for i in range(4, 10):
    for j in range(i):
        t.forward(100)
        t.right(360/i)
        j += 1
    t.pencolor((randint(1, 255), randint(1, 255), randint(1, 255)))
    i += 1
