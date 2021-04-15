from turtle import *

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(50)


def move_backward():
    t.back(50)


def move_clockwise():
    t.right(50)


def move_anticlockwise():
    t.left(50)


def clear():
    t.home()
    t.clear()
    t.home()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_anticlockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
