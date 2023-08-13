from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10 # x move 10px at a time
        self.y_move = 10 # y move 10px at a time
        self.move_speed = 0.1
    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # when it bounce it goes opposite direction => -10
        self.y_move *= -1

    def bounce_x(self): # when paddle hit the ball
        self.x_move *= -1
        self.move_speed -= 0.007 # sleep less, speed up

    def reset_position(self):
        self.goto(0, 0)
        #self.move_speed = 0.02 #reset the game, reset the move speed
        self.bounce_x()