from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(0,272.5)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,30)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0,-30)
        self.write(f"YOUR SCORE IS: {self.score}", align=ALIGNMENT, font=FONT)
