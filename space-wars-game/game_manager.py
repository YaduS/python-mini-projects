from time import sleep
from turtle import Screen

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
MAX_Y = +WINDOW_HEIGHT / 2
MIN_Y = -WINDOW_HEIGHT / 2

RENDER_DELAY = 1


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.config_main_screen()

    def config_main_screen(self):
        screen = self.screen
        screen.title("Space Wars Clone")
        screen.bgcolor("black")
        screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        screen.tracer(0)

    def start_game_loop(self):
        game_active = True
        while game_active:
            self.screen.update()

            sleep(RENDER_DELAY)
