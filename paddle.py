from turtle import Turtle


class Paddle:
    def __init__(self):
        paddle1 = self.create_paddle(350, 0)
        paddle2 = self.create_paddle(-350, 0)

    def create_paddle(self, x_pos, y_pos):
        width = 20
        height = 100
        paddle = Turtle("square")
        paddle.resizemode("user")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.color("black")
        paddle.speed("fastest")
        paddle.penup()
        paddle.goto(x_pos, y_pos)

    def up(self):
        pass
