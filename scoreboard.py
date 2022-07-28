from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # убирает курсор с экрана
        self.penup()
        self.level = 1
        self.color("black")
        self.goto(-270, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level:  {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
