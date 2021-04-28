from turtle import *


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        # self.goto(0,0)
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.1
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.y_move *= -1

    def bounce_horizontal(self):
        self.x_move *= -1
        self.movement_speed *= 0.5

    def reset_game(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.movement_speed = 0.1

