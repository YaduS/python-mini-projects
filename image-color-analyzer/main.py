from PIL import Image
from numpy import array
from typing import List


def convert_to_hex(rgb_list: List[int]):
    r, g, b = rgb_list
    hex_code = f"#{r:02X}{g:02X}{b:02X}"
    return hex_code


def main():
    img = Image.open("./image-color-analyzer/color-sample.jpg")
    img_ndarray = array(img)

    # expect the array shape to be something like width x height x 3 (one each for R , G and B)
    print(img_ndarray.shape)

    # convert and flatten to a single dimensional array and convert each rgb to hex
    hex_array = [convert_to_hex(item) for row in img_ndarray for item in row]
    print(hex_array[0], hex_array[1], len(hex_array))


if __name__ == "__main__":
    main()
