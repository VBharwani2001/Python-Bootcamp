from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-220, 250)
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", False, "center", FONT)

    def game_over_screen(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
