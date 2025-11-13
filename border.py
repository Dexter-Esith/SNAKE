from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(270, -270)
        self.pendown()
        self.pensize(1)
        self.pencolor('red')
        self.speed("fastest")
        self.draw_border()

    def draw_border(self):
        for _ in range(4):
            self.left(90)
            self.forward(540)