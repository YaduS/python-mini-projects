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


def check_ball_bounce(ball: Ball):
    padding = 20
    (x, y) = ball.pos()
    if x > WINDOW_WIDTH / 2 - padding or x < -WINDOW_WIDTH / 2 + padding:
        ball.bounce_x()
    if y > WINDOW_HEIGHT / 2 - padding or y < -WINDOW_HEIGHT / 2 + padding:
        ball.bounce_y()


def main():
    config_main_screen(screen)
    create_blocks()

    ball = Ball()
    game_active = True
    counter = 0
    while game_active:
        screen.update()

        ball.move()
        check_ball_bounce(ball)

        time_delay = 1 / ball.ball_speed
        sleep(time_delay)


if __name__ == "__main__":
    main()
