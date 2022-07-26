from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def eat_food(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

