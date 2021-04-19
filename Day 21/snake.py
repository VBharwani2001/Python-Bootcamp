from turtle import *
start_position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for position in start_position:
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.turtles.append(turtle)

    def move(self):
        for turtle in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turtle-1].xcor()
            new_y = self.turtles[turtle-1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def up(self):
        self.turtles[0].setheading(90)

    def down(self):
        self.turtles[0].setheading(270)

    def left(self):
        self.turtles[0].setheading(180)

    def right(self):
        self.turtles[0].setheading(0)
