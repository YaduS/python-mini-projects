from PIL import Image
from PIL import ImageDraw


def open_image():
    with open("sample.jpg", "rb") as fp:
        im = Image.open(fp)
        im.show()  # this opens image in default image view desktop app?


def main():
    open_image()


if __name__ == "__main__":
    main()
