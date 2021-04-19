from turtle import *
import time
import snake
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = snake.Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameison = True
while gameison:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
