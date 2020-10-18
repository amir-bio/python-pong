import turtle
import winsound

def make_paddle():
    paddle = turtle.Turtle()
    paddle.speed(0) # set speed of animation to max
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup() # don't draw a line as it moves
    # store score for each player on paddle as paddle represents the player
    paddle.score = 0
    return paddle

wm = turtle.Screen()
wm.title("Pong")
wm.bgcolor("black")
wm.setup(width=800, height=600)

# stops automatic updating and require manual update of screen, leads to faster
# program
wm.tracer(0)

# left paddle
paddle_a = make_paddle()
paddle_a.goto(-350, 0)

# right paddle
paddle_b = make_paddle()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0) # set speed of animation to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball.dy = 2

# score text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def paddle_up(paddle):
    paddle.sety(paddle.ycor()+20)

def paddle_down(paddle):
    paddle.sety(paddle.ycor()-20)

def bounce_sound():
    # play the sound asynchronously to ensure the main animation is not paused/delayed
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

wm.listen()
wm.onkeypress(lambda: paddle_up(paddle_a), "w")
wm.onkeypress(lambda: paddle_down(paddle_a), "s")

# arrow keys for the righty paddle
wm.onkeypress(lambda: paddle_up(paddle_b), "Up")
wm.onkeypress(lambda: paddle_down(paddle_b), "Down")

def animate():
    """"Animate a frame of the game with all the required logic and call ontimer to animate next frame"""
    wm.update()
    pen.clear()
    pen.write(f"Player A: {paddle_a.score} Player B: {paddle_b.score}", align="center", font=("Courier", 24 , "normal"))

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check - bounce from top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        bounce_sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounce_sound()

    # if the ball has gone past the paddles go to the center and reverse direction
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        paddle_a.score += 1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        paddle_b.score += 1

    # handle collision with paddle
    if ball.xcor() > 340 and  ball.xcor() < 350 and paddle_b.ycor() - 40 < ball.ycor() < paddle_b.ycor() + 40:
        ball.dx *= -1
        bounce_sound()

    if ball.xcor() < -340 and  ball.xcor() > -350 and paddle_a.ycor() - 40 < ball.ycor() < paddle_a.ycor() + 40:
        ball.dx *= -1
        bounce_sound()

    wm.ontimer(animate, 10) # call animate again after 10ms (=> 100 fps)

wm.ontimer(animate)
wm.mainloop()
