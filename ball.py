from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.s_x=10
        self.s_y=10
        self.move_speed = 0.1

    def move(self):
        n_x = self.xcor() + self.s_x
        n_y = self.ycor() + self.s_y
        self.goto(n_x,n_y)

    def bounce_y(self):
        self.s_y = -1 * self.s_y

    def bounce_x(self):
        self.s_x = -1 * self.s_x
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
