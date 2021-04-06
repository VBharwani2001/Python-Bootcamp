import turtle
from turtle import *
from random import *
t = Turtle()
screen = Screen()
screen.colormode(255)
# t.circle(100)
# t.heading()
# print(t.heading())
# print(t.position())
# t.setheading(95)
# t.circle(100)

t.speed(0)


def draw_circles():
    for i in range(0, 72):
        t.setheading(i*5)
        t.circle(100)
        t.pencolor((randint(1, 255), randint(1, 255), randint(1, 255)))


draw_circles()

print(t.heading())
turtle.done()
