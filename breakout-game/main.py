from turtle import Screen, _Screen


screen = Screen()


def config_main_screen(screen: _Screen):
    screen.title("Breakout Clone")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    screen.onkeypress(fun=lambda: screen.bye(), key="Escape")
    screen.listen()


def main():
    config_main_screen(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()
