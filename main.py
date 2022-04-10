import turtle

# windows
wn = turtle.Screen()
wn.title("pong by Amit Halfon")
wn.bgcolor("#EBDEF0")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#1B2631")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # size
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#1B2631")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # size
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#1B2631")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.20  # data change x
ball.dy = -0.20  # data change y


# func
def paddle_a_up():
    if paddle_a.ycor() <= 240:  # for border
        y = paddle_a.ycor()
        y += 20  # up
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() >= -230:
        y = paddle_a.ycor()
        y -= 20  # up
        paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() <= 240:
        y = paddle_b.ycor()
        y += 20  # up
        paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() >= -230:
        y = paddle_b.ycor()
        y -= 20  # up
        paddle_b.sety(y)


# keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "S")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeyrelease(wn.bye, "Escape")

# main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.goto(0, 0)  # new round
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.goto(0, 0)  # new round
        ball.dx *= -1

    # paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
