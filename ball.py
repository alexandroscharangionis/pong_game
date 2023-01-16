from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # to be used with time.sleep()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
       # Multiplying by -1 always reverses direction on Y axis (bounce effect)
        self.y_move *= -1

    def bounce_x(self):
       # Multiplying by -1 always reverses direction on X axis (bounce effect)
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
