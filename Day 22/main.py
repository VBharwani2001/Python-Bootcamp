from turtle import *
from paddle import Paddle
from ball import Ball
import time
import scoreboard
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
scoreboard = scoreboard.Scoreboard()

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    time.sleep(ball.movement_speed)
    ball.move_ball()
    # CHECK COLLISION WITH TOP AND BOTTOM WALL
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_vertical()
    # CHECK BALL CONTACT WITH PADDLES
    if (ball.distance(r_paddle) < 50 and ball.xcor() >= 325) or (ball.xcor() <= -340 and ball.distance(l_paddle) < 50):
        print("contact")
        #ball.x_move += 5
        ball.bounce_horizontal()
    # CHECK IF PADDLE MISS THE BALL
    if ball.xcor() > 400:
        ball.reset_game()
        scoreboard.l_score += 1
    if ball.xcor() < -400:
        ball.reset_game()
        scoreboard.r_score += 1

    screen.update()
screen.exitonclick()
