from PIL import Image, ImageDraw, ImageFont
import os


class ImageProcessor:

    def __init__(self, full_filepath) -> None:

        filename_with_extension = os.path.basename(full_filepath)
        name_without_extension = os.path.splitext(filename_with_extension)[0]

        self.filename = name_without_extension
        self.img = Image.open(full_filepath)
        self.watermarked_img = None

        print("image dimensions:", self.img.size)

    def open_new_image(self, newFilename) -> None:
        self.img = Image.open(newFilename)

    def show(self):
        self.img.show()

    def save(self):
        self.img.save("sample-converted.jpg")

    def watermark(self, text="Made with Pillow!"):
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", self.img.size, (255, 255, 255, 0))

        # get a drawing context
        d = ImageDraw.Draw(self.img)

        # let watermark position be 20% of height above bottom, and 10% width from left
        (width, height) = self.img.size
        top = height * (1 - 0.2)
        left = width * 0.1

        # get a font size equal to 3.75% of width? why not
        font_size = 3.75 / 100 * width
        # get a font
        fnt = ImageFont.truetype("arial.ttf", font_size)

        # draw text in half opacity
        d.text((left, top), text, font=fnt, fill=(255, 255, 255, 128))

        out = Image.alpha_composite(self.img.convert("RGBA"), txt)
        self.watermarked_img = out

    def save_watermarked_img(self):
        watermarked_image_name = f"{self.filename}-watermarked.jpg"

        # "YCbCr" is essentially JPEG?
        # https://pillow.readthedocs.io/en/latest/handbook/concepts.html#modes
        self.watermarked_img.convert(mode="YCbCr").save(watermarked_image_name)
        return watermarked_image_name
