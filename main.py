import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

#create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0) # turn off tracer


#create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = ScoreBoard()


ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()  # only update after finishing set up
    ball.ball_move()

    #DETEC COLLISION WITH THE WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()


    #DETECT COLLISION WITH RIGHT PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect r_paddle misses
    if ball.xcor() > 380: #on the right side
        ball.reset_position()
        scoreboard.l_point()


    #Detect l_paddle misses
    if ball.xcor() < -380:  # on the left side
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()