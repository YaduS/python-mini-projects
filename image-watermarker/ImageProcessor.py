from PIL import Image
from PIL import ImageDraw


class ImageProcessor:

    def __init__(self, filename) -> None:
        self.im = Image.open(filename)

    def open_new_image(self, newFilename) -> None:
        self.im = Image.open(newFilename)

    def show(self):
        self.im.show()

    def save(self):
        self.im.save("sample-converted.jpg")
