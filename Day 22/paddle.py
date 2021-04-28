from turtle import *

positions = [(350, 0), (-350, 0)]
paddles = []


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        paddles.append(paddles)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
