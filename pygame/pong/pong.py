import turtle

import pygame

# Pygame
pygame.mixer.init()

# Create a screen position and color
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Doesn't draw a line (Because turtle normally draw a line)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Doesn't draw a line (Because turtle normally draw a line)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")

# Doesn't draw a line (Because turtle normally draw a line)
ball.penup()
ball.goto(0, 0)

# Ball moving every one pixels, since X is positive it will
# move to right and since Y is positive it will move up
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="Center",
          font=("Courier", 24, "normal"))


def paddle_a_up():
    # Return a Y coordinate to Y
    y = paddle_a.ycor()
    # Plus 20 to Y
    y += 20
    # Set Y
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


def tick():
    global score_a
    global score_b
    wn.ontimer(tick, 10)

    # Move the ball, setting the ball coordinate and getting
    # current coordinate and plus with ball.dx, so the ball
    # will move right and up (X, Y)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        pygame.mixer.music.load("bounce.wav")
        pygame.mixer.music.play()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        pygame.mixer.music.load("bounce.wav")
        pygame.mixer.music.play()

    # Go off the screen and reserve direction (Left and Right)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="Center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="Center", font=("Courier", 24, "normal"))

    # Paddle and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        pygame.mixer.music.load("bounce.wav")
        pygame.mixer.music.play()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        pygame.mixer.music.load("bounce.wav")
        pygame.mixer.music.play()

    wn.update()


tick()
wn.mainloop()
