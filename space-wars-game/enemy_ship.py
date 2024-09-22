from turtle import _Screen, Turtle
from game_constants import MIN_Y
from typing import List

MOVE_SPEED = 2.5
PROJECTILE_SPEED = 5
MAX_MOVE_COUNTER = 90
STARTING_POSITION = (0, 240)


class EnemyShip(Turtle):

    def __init__(self):
        super().__init__()
        self.projectiles: List[Turtle] = []
        self.move_direction = "left"
        self.move_counter = 1
        self.set_shape()

    def set_shape(self):
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape("./space-wars-game/spaceship.gif")
        self.resizemode("user")
        self.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=0)
        self.left(90)

    def create_projectile(self):
        rocket = Turtle(shape="square")
        rocket.penup()
        rocket.setposition((self.xcor(), self.ycor() - 20))
        rocket.color("red")
        rocket.resizemode("user")
        rocket.shapesize(stretch_wid=0.5, stretch_len=0.1, outline=0)
        self.projectiles.append(rocket)

    def move_existing_projectiles(self):
        projectiles_to_remove = []
        for i, projectile in enumerate(self.projectiles):
            ycor = (
                projectile.ycor() - PROJECTILE_SPEED
                if projectile.ycor() > MIN_Y
                else projectile.ycor()
            )
            if ycor <= MIN_Y:
                projectiles_to_remove.append(i)
            else:
                projectile.goto(x=projectile.xcor(), y=ycor)

        for index in projectiles_to_remove[::-1]:
            print("index: ", index)
            self.projectiles[index].clear()
            self.projectiles[index].hideturtle()
            del self.projectiles[index]

    def fire(self):
        self.create_projectile()

    def move_ship(self):
        xcor = self.xcor()
        xcor = xcor - MOVE_SPEED if self.move_direction == "left" else xcor + MOVE_SPEED
        self.goto(x=xcor, y=self.ycor())

    def cycle_update(self):
        self.move_counter += 1
        if not (self.move_counter % (MAX_MOVE_COUNTER // 3)):
            self.move_ship()

        if not (self.move_counter % MAX_MOVE_COUNTER):
            self.move_direction = "left" if self.move_direction == "right" else "right"
            self.move_counter = 1
