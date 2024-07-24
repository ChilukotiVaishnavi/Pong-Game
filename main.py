from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from win import Player
import time

screen = Screen()
screen.screensize(850, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Paddle((290,0))
l_paddle = Paddle((-290,0))
ball = Ball()

player = Player()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>250 or ball.ycor()<-250:
        ball.bounce_y()
    if (ball.distance(r_paddle)<50 and ball.xcor()>270) or (ball.distance(l_paddle)<50 and ball.xcor()<-270):
        ball.bounce_x()
    elif (ball.xcor()>280):
        ball.reset_pos()
        player.p1()
    elif (ball.xcor()<-280):
        ball.reset_pos()
        player.p2()

screen.exitonclick()

