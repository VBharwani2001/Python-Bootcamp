import turtle

timmy_the_turtle = turtle.Turtle()
screen = turtle.Screen()
timmy_the_turtle.shape("turtle")

i = 0
while i < 4:
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    i += 1

screen.onclick("close")
