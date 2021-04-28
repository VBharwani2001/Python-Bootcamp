import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
car = CarManager()
scoreboard = Scoreboard()
speed = 0.1
screen.onkeypress(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(speed)
    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over_screen()

    if player.ycor() >= 300:
        player.detect_finish()
        speed *= 0.5
        scoreboard.increase_score()


    screen.update()

screen.exitonclick()
