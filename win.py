from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l,self.r=0,0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 180)
        self.write(self.r, align="center", font=("Courier", 60, "normal"))

    def p1(self):
        self.l+=1
        self.scoreboard()




    def p2(self):
        self.r+=1
        self.scoreboard()
