from PIL import Image
import numpy as np
from typing import List


def convert_to_hex(rgb_list: List[int]):
    r, g, b = rgb_list
    hex_code = f"#{r:02X}{g:02X}{b:02X}"
    return hex_code


def find_top_colors(hex_array: List[str]):

    # return unique values and counts of corresponding values
    values, counts = np.unique(hex_array, return_counts=True)

    # sort counts and return values in descending order
    sorted_indices = np.argsort(counts)[::-1]
    sorted_values = values[sorted_indices]
    # sorted_counts = counts[sorted_indices]
    # print(f"sorted_counts: {sorted_counts[:10]}")

    # TODO: 1. calculated euclidean distance between colors and shrink array based on a delta value

    # return top 10 sorted values
    return sorted_values[:10]


def main():
    img = Image.open("./image-color-analyzer/color-sample.jpg")
    img_ndarray = np.array(img)

    # expect the array shape to be something like width x height x 3 (three cause one each for R , G and B)
    height, width, _ = img_ndarray.shape
    print(f"resolution: {width} x {height}")

    # convert and flatten to a single dimensional array and convert each rgb to hex
    hex_colors = [convert_to_hex(item) for row in img_ndarray for item in row]
    top_colors = find_top_colors(hex_colors)

    print(f"top_colors: {top_colors}")


if __name__ == "__main__":
    main()


# TODO: 2. make GUI so that:
# a) images can be selected with a file selector
# b) top 10 colors can be displayed in the UI visually alongside the image preview;
# c) delta value for color variance can be input through ui and button to rerun calculations based on new delta
