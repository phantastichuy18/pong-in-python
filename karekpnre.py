import turtle
import winsound
import tkinter as tk

bgcolor = "#2b90ca"
greey = "#13222a"
wd = turtle.Screen()
wd.title("Pong in Python")
wd.bgcolor(bgcolor)
wd.setup(1000, 650)
score_1 = 0
score_2 = 0

pong = turtle.Turtle()
pong.color("white")
pong.penup()
pong.hideturtle()
pong.goto(0, 235)
pong.write("PONG GAME", align="center", font=("FFF Forward", 24, "normal"))

bd = turtle.Turtle()
bd.shape("square")
bd.speed(5)
bd.penup()
bd.goto(-400, 220)
bd.pendown()
bd.goto(400, 220)
bd.goto(400, -220)
bd.goto(-400, -220)
bd.goto(-400, 220)
bd.penup()
bd.goto(0, 220)
bd.right(90)
for i in range(30):
    bd.pendown()
    bd.forward(10)
    bd.penup()
    bd.forward(5)
bd.hideturtle()

winsound.PlaySound('start.wav', winsound.SND_ASYNC)

paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color(greey)
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color(greey)
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 80)
score_display.write("0              0", align="center", font=("FFF Forward", 24, "normal"))

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color(greey)
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y += -20
    paddle1.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y += -20
    paddle2.sety(y)

wd.listen()
wd.onkeypress(paddle1_up, 'w')
wd.onkeypress(paddle1_down, 's')
wd.onkeypress(paddle1_up, 'W')
wd.onkeypress(paddle1_down, 'S')
wd.onkeypress(paddle2_up, 'Up')
wd.onkeypress(paddle2_down, 'Down')

while True:
    wd.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if paddle1.ycor() > 165:
        print("hello")

    if ball.ycor() > 210 or ball.ycor() < -210:
        winsound.PlaySound('wall.wav', winsound.SND_ASYNC)
        ball.dy *= -1

    if ball.xcor() > 390:
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        score_display.clear()
        score_display.write("{}              {}".format(score_1, score_2),  align="center", font=("FFF Forward", 24, "normal"))

    if ball.xcor() < -390:
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        score_display.clear()
        score_display.write("{}              {}".format(score_1, score_2),  align="center", font=("FFF Forward", 24, "normal"))
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 60 and ball.ycor() > paddle2.ycor() -60):
        winsound.PlaySound('paddle.wav', winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 60 and ball.ycor() > paddle1.ycor() -60):
        winsound.PlaySound('paddle.wav', winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1