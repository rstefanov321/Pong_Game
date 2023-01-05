from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("###THIS IS THE PONG GAME###")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Score((200, 200))
l_score = Score((-200, 200))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    # Detect when right paddle misses
    elif ball.xcor() > 380:
        print("point to left Paddle! ")
        l_score.add_point()
        ball.reset_position()
        # game_is_on = False

    # Detect when left paddle misses
    elif ball.xcor() < -380:
        print("point to right Paddleee")
        r_score.add_point()
        ball.reset_position()
        # game_is_on = False





screen.exitonclick()
