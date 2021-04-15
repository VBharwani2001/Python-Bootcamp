from turtle import *
import random
colours = ["green", "yellow", "blue", "red", "orange", "purple"]
y_index = [-110, -70, -30, 10, 50, 90]
turtle_name = []
screen = Screen()
screen.setup(500, 400)


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_index[turtle_index])
    turtle_name.append(new_turtle)
user_guess = screen.textinput("Make your bet", "Which colour will WIN: ")
if user_guess:
    race_on = True

while race_on:
    for turtle in turtle_name:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
        # print(turtle.xcor())
        if (turtle.xcor() >= 230):
            race_on = False
            winning_turtle = turtle.pencolor()
            print(turtle.pencolor())
# timmy_green = Turtle()
# timmy_yellow = Turtle()
# timmpy_blue = Turtle()
# timmy_red = Turtle()
# timmpy_orange = Turtle()
# timmy_purple = Turtle()

# timmy_green.color("green")
# timmy_green.penup()
# timmy_green.goto(-240, 10)
# timmy_green.shape("turtle")

# timmy_yellow.color("yellow")
# timmy_yellow.penup()
# timmy_yellow.goto(-240, 50)
# timmy_yellow.shape("turtle")

# timmpy_blue.color("blue")
# timmpy_blue.penup()
# timmpy_blue.goto(-240, -30)
# timmpy_blue.shape("turtle")

# timmy_red.color("red")
# timmy_red.penup()
# timmy_red.goto(-240, -70)
# timmy_red.shape("turtle")

# timmpy_orange.color("orange")
# timmpy_orange.penup()
# timmpy_orange.goto(-240, -110)
# timmpy_orange.shape("turtle")

# timmy_purple.color("purple")
# timmy_purple.penup()
# timmy_purple.goto(-240, 90)
# timmy_purple.shape("turtle")

if (winning_turtle == user_guess):
    screen.clear()
    turtle = Turtle()
    turtle.setpos(0, 0)
    turtle.write("YOU LOSE")
else:
    screen.clear()
    turtle = Turtle()
    turtle.setpos(0, 0)
    turtle.write("YOU LOSE")
print(user_guess)
screen.exitonclick()
