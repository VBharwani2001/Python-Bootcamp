from turtle import *
from random import *
t = Turtle()
direction = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)
t.pensize(15)
t.shapesize(1)
for _ in range(100):
    t.forward(20)
    t.right(choice(direction))
    t.pencolor((randint(1, 255), randint(1, 255), randint(1, 255)))

t.onclick()
