from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.penup()
