from time import sleep
from turtle import Screen
from main_ship import MainShip
from enemy_ship import EnemyShip
from game_constants import WINDOW_HEIGHT, WINDOW_WIDTH, RENDER_DELAY


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.config_main_screen()
        self.create_game_elements()

    def create_game_elements(self):
        self.screen.register_shape("./space-wars-game/spaceship.gif")
        self.main_ship = MainShip(screen=self.screen)
        self.enemy_ship = EnemyShip()

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

            self.main_ship.cycle_update()
            self.enemy_ship.cycle_update()
            sleep(RENDER_DELAY)
