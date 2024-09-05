from turtle import Screen, _Screen
from time import sleep
from turtle import Turtle
from typing import List

from ball import Ball
from block import Block
from paddle import Paddle

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NO_OF_ROWS = 3
ROW_COLORS = ["green", "red", "yellow"]
NO_OF_BLOCK_PER_ROW = 4
DEFAULT_BLOCK_HEIGHT = 5


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.paddle_bottom = None
        self.paddle_top = None
        self.blocks: List[List[Turtle]] = []

        self.config_main_screen()
        self.create_blocks()

        self.create_paddles()
        self.config_listeners()

        self.ball = Ball()

    def config_main_screen(self):
        screen = self.screen
        screen.title("Breakout Clone")
        screen.bgcolor("black")
        screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        screen.tracer(0)

    def create_paddles(self):
        self.paddle_bottom = Paddle(color="aqua")
        self.paddle_top = Paddle(starting_position=(0, 280), color="orange")

    def config_listeners(self):
        screen = self.screen

        # keys to move left
        for key in ["Left", "a", "A"]:
            screen.onkeypress(
                fun=lambda: (
                    self.paddle_bottom.move_left(),
                    self.paddle_top.move_left(),
                ),
                key=key,
            )

        # keys to move right
        for key in ["Right", "d", "D"]:
            screen.onkeypress(
                fun=lambda: (
                    self.paddle_bottom.move_right(),
                    self.paddle_top.move_right(),
                ),
                key=key,
            )

        screen.onkeypress(fun=lambda: screen.bye(), key="Escape")
        screen.listen()

    def create_blocks(self):
        for i in range(NO_OF_ROWS):
            self.blocks.append([])
            for j in range(NO_OF_BLOCK_PER_ROW):
                self.blocks[i].append(
                    Block(
                        starting_position=(-305 + (j * 200), -30 + (i * 30)),
                        color=ROW_COLORS[i],
                    )
                )

    def check_ball_bounce(self):
        padding = 20
        (x, y) = self.ball.pos()
        if x > WINDOW_WIDTH / 2 - padding or x < -WINDOW_WIDTH / 2 + padding:
            self.ball.bounce_x()
        if y > WINDOW_HEIGHT / 2 - padding or y < -WINDOW_HEIGHT / 2 + padding:
            self.ball.bounce_y()

    def check_block_collision(self):

        ball_y = self.ball.ycor()
        for blocks_row in self.blocks:
            for ind, block in enumerate(blocks_row):
                if block == None:
                    continue

                radial_distance = self.ball.distance(block)
                block_y = block.ycor()
                y_distance = abs(block_y - ball_y)
                # print(radial_distance, y_distance, block_y, y)

                # Note: Had to do some experimentation to get the constants used below
                if radial_distance < 110 and y_distance < 25:
                    self.ball.bounce_y()
                    block.clear()
                    block.hideturtle()
                    blocks_row[ind] = None
                    break

    def start_game_loop(self):
        game_active = True
        while game_active:
            self.screen.update()

            self.ball.move()
            self.check_ball_bounce()
            self.check_block_collision()

            time_delay = 1 / self.ball.ball_speed / 10
            sleep(time_delay)
