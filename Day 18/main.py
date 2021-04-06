import turtle
from turtle import *
from random import *
t = Turtle()
screen = Screen()
screen.colormode(255)


def colour_gen():
    return (randint(1, 255), randint(1, 255), randint(1, 255))


t.speed(0)

t.penup()
t.goto(-300, -300)


def draw():
    t.speed(0)

    for i in range(1, 50):
        for j in range(30):
            t.pendown()
            t.dot(12, colour_gen())
            t.penup()
            t.forward(20)
        t.setposition(-300, -300 + 20*i)


draw()
turtle.done()
