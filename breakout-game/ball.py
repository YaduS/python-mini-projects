from turtle import Turtle

BALL_MOVE_DISTANCE = 2
BALL_SPEED = 10
STARTING_POSITION = (0, -240)


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.setposition(STARTING_POSITION[0], STARTING_POSITION[1])
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)

        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = BALL_MOVE_DISTANCE
        self.ball_speed = BALL_SPEED

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def move(self):
        (x, y) = self.pos()
        self.goto((x + self.x_move, y + self.y_move))

    # def reset_position(self):
    #     self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
    #     self.ball_speed = BALL_SPEED

    # def increase_speed(self):
    #     self.ball_speed += 2
