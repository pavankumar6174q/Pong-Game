from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width= 1200, height= 700)
screen.title("PONG")
screen.tracer(0) #this helps remove the animation delay

ball = Ball()
score = ScoreBoard()


r_paddle = Paddle((550, 0))
l_paddle = Paddle((-550, 0))
screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
   # bouncing of the top and botton walls
    if ball.ycor()> 300 or ball.ycor()< -300:
        ball.bounce_y()
    
    #bouncing of the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor()> 520 or ball.distance(l_paddle) < 50 and ball.xcor()< -520:
        print("contact")
        ball.bounce_x()
    

    #ball missed  right
    if ball.xcor() > 580:
        ball.reset()
        score.l_point()
#ball missed left
    if ball.xcor()< -580:
        ball.reset()
        score.r_point()















screen.exitonclick()