from turtle import Screen, _Screen
from block import Block

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NO_OF_ROWS = 3
ROW_COLORS = ["green", "red", "yellow"]
NO_OF_BLOCK_PER_ROW = 4
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
    blocks = []
    for i in range(NO_OF_ROWS):
        blocks.append([])
        for j in range(NO_OF_BLOCK_PER_ROW):
            blocks[i].append(
                Block(
                    starting_position=(-305 + (j * 200), -30 + (i * 30)),
                    color=ROW_COLORS[i],
                )
            )


def main():
    config_main_screen(screen)
    create_blocks()
    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    main()
