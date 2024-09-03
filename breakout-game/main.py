from turtle import Screen, _Screen
from block import Block

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NO_OF_ROWS = 3
NO_OF_BLOCK_PER_ROW = 8
DEFAULT_BLOCK_HEIGHT = 5

# todo: maybe move below line of code inside main function?
screen = Screen()


def config_main_screen(screen: _Screen):
    screen.title("Breakout Clone")
    screen.bgcolor("black")
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.tracer(0)

    # bind
    screen.onkeypress(fun=lambda: screen.bye(), key="Escape")
    screen.listen()


def create_blocks():
    # block_width = WINDOW_WIDTH / 3 / 3
    # block_height = DEFAULT_BLOCK_HEIGHT
    # block = Block((x_pos, y_pos))
    block = Block(starting_position=(0, 0), color="green")
    block = Block((50, 20), "red")
    block = Block((-50, -20), "yellow")


def main():
    config_main_screen(screen)
    create_blocks()
    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    main()
