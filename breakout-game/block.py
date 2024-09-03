from turtle import Turtle


class Block(Turtle):

    def __init__(self, starting_position, color="white"):
        super().__init__()
        self.penup()
        self.setposition(starting_position)
        self.shape("square")
        self.color(color)
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5, outline=0)

    def destroy_block(self):
        pass
