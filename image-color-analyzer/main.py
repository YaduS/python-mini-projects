from PIL import Image
from numpy import array


def main():
    img = Image.open("./image-color-analyzer/color-sample.jpg")
    img_ndarray = array(img)
    print(img_ndarray.shape)
    pass


if __name__ == "__main__":
    main()
