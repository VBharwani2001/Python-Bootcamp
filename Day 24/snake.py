from turtle import *
start_position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in start_position:
            self.add_snake(position)

    def add_snake(self, position):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend_snake(self):
        self.add_snake(self.turtles[-1].position())

    def move(self):
        for turtle in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turtle-1].xcor()
            new_y = self.turtles[turtle-1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def reset(self):
        for turtle in self.turtles:
            turtle.hideturtle()
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def up(self):
        self.turtles[0].setheading(90)

    def down(self):
        self.turtles[0].setheading(270)

    def left(self):
        self.turtles[0].setheading(180)

    def right(self):
        self.turtles[0].setheading(0)
