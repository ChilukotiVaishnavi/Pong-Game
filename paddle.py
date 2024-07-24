from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pos)
        self.p = 20
    def go_up(self):
        y = self.ycor() + self.p
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - self.p
        self.goto(self.xcor(), y)