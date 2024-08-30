from ImageProcessor import ImageProcessor


def open_image():
    imgObj = ImageProcessor("sample.jpg")
    imgObj.watermark()


def main():
    open_image()


if __name__ == "__main__":
    main()
