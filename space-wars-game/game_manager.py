from time import sleep
from turtle import Screen
from typing import List

from main_ship import MainShip
from enemy_ship import EnemyShip
from game_constants import (
    MAX_Y,
    NO_OF_ENEMIES_PER_ROW,
    NO_OF_ENEMY_ROWS,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    RENDER_DELAY,
)


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.config_main_screen()
        self.create_game_elements()

    def create_game_elements(self):
        self.screen.register_shape("./space-wars-game/spaceship.gif")
        self.main_ship = MainShip(screen=self.screen)

        self.generate_enemy_ships()

    def generate_enemy_ships(self):
        # note: tweak hardcoded values in this file to change placement of enemy ships. Its better to get these constants either from constants file or better yet as static properties of something from the enemy_ship file?
        self.enemy_ships: List[EnemyShip] = []
        for i in range(NO_OF_ENEMY_ROWS):
            for j in range(NO_OF_ENEMIES_PER_ROW):
                ypos = MAX_Y - 50 - (i * 100)
                xpos = -j * 50 if j % 2 else (j + 1) * 50
                self.enemy_ships.append(EnemyShip((xpos, ypos)))

    def config_main_screen(self):
        screen = self.screen
        screen.title("Space Wars Clone")
        screen.bgcolor("black")
        screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        screen.tracer(0)

    def cycle_update(self):

        self.main_ship.cycle_update()
        for enemy_ship in self.enemy_ships:
            enemy_ship.cycle_update()

    def start_game_loop(self):
        game_active = True
        while game_active:
            self.screen.update()
            self.cycle_update()
            sleep(RENDER_DELAY)
