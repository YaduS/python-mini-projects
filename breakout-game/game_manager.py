from turtle import Screen, _Screen
from block import Block
from time import sleep
from ball import Ball

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NO_OF_ROWS = 3
ROW_COLORS = ["green", "red", "yellow"]
NO_OF_BLOCK_PER_ROW = 4
DEFAULT_BLOCK_HEIGHT = 5


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.config_main_screen()

        self.blocks = []
        self.create_blocks()

        self.ball = Ball()

    def config_main_screen(self):
        screen = self.screen
        screen.title("Breakout Clone")
        screen.bgcolor("black")
        screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        screen.tracer(0)

        # bind
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

    def start_game_loop(self):
        game_active = True
        while game_active:
            self.screen.update()

            self.ball.move()
            self.check_ball_bounce()

            time_delay = 1 / self.ball.ball_speed
            sleep(time_delay)
