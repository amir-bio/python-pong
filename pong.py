import turtle

wm = turtle.Screen()
wm.title("Pong")
wm.bgcolor("black")
wm.setup(width=800, height=600)

# stops automatic updating and require manual update of screen, leads to faster
# program
wm.tracer(0)

# left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set speed of animation to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # don't draw a line as it moves
paddle_a.goto(-350, 0)
paddle_a.score = 0

# right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set speed of animation to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.score = 0

# ball
ball = turtle.Turtle()
ball.speed(0) # set speed of animation to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Play A: {paddle_a.score} Player B: {paddle_b.score}", align="center", font=("Courier", 24 , "normal"))


def paddle_up(paddle):
    y = paddle.ycor()
    paddle.sety(y+20)

def paddle_down(paddle):
    y = paddle.ycor()
    paddle.sety(y-20)

wm.listen()
wm.onkeypress(lambda: paddle_up(paddle_a), "w")
wm.onkeypress(lambda: paddle_down(paddle_a), "s")

# arrow keys for the righty paddle
wm.onkeypress(lambda: paddle_up(paddle_b), "Up")
wm.onkeypress(lambda: paddle_down(paddle_b), "Down")

# main game loop
while True:
    wm.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check - bounce from top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # if the ball has gone past the paddle go to the center and reverse direction
    if ball.xcor() > 390 or  ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # handle collision with paddle
    if ball.xcor() > 340 and  ball.xcor() < 350 and paddle_b.ycor() - 40 < ball.ycor() < paddle_b.ycor() + 40:
        ball.dx *= -1

    if ball.xcor() < -340 and  ball.xcor() > -350 and paddle_a.ycor() - 40 < ball.ycor() < paddle_a.ycor() + 40:
        ball.dx *= -1
