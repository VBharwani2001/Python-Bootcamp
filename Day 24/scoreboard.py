from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0

        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 18, "normal"))

    def game_over_screen(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, "center", ("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()