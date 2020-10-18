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

# right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set speed of animation to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0) # set speed of animation to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

def paddle_up(paddle):
    y = paddle.ycor()
    paddle.sety(y+20)

def paddle_down(paddle):
    y = paddle.ycor()
    paddle.sety(y-20)

wm.listen()
wm.onkeypress(lambda: paddle_up(paddle_a), "w")
wm.onkeypress(lambda: paddle_down(paddle_a), "s")

wm.onkeypress(lambda: paddle_up(paddle_b), "Up")
wm.onkeypress(lambda: paddle_down(paddle_b), "Down")

# main game loop
while True:
    wm.update()
    wm
