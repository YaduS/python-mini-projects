from turtle import Turtle

STARTING_POSITION = (0, -380)

WINDOW_MAX_X = 320
WINDOW_MIN_X = -320

MOVE_SPEED = 30


class Paddle(Turtle):

    def __init__(self, starting_position=STARTING_POSITION, color="white"):
        super().__init__()

        self.penup()
        self.setposition(starting_position)
        self.shape("square")
        self.color(color)
        self.resizemode("user")
        self.shapesize(stretch_len=8, stretch_wid=1, outline=0)

    def move_left(self):
        xcor = self.xcor()
        if xcor > WINDOW_MIN_X:
            self.goto(x=xcor - MOVE_SPEED, y=self.ycor())

    def move_right(self):
        xcor = self.xcor()
        if xcor < WINDOW_MAX_X:
            self.goto(x=xcor + MOVE_SPEED, y=self.ycor())
