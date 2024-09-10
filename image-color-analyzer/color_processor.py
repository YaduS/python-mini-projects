from PIL import Image, ImageFile
import numpy as np
from typing import List

COLOR_DELTA = 24


class ColorProcessor:

    def __init__(self):
        self.img: ImageFile = None
        self.delta = 1

    def load_image(self, img: ImageFile):
        self.img = img

    def analyze_image(self, delta: int):
        if self.img == None:
            return None

        self.delta = delta
        # TODO: implement delta in calculations

        img_ndarray = np.array(self.img)

        # expect the array shape to be something like width x height x 3 (three cause one each for R , G and B)
        height, width, _ = img_ndarray.shape
        print(f"resolution: {width} x {height}")

        # convert and flatten to a single dimensional array and convert each rgb to hex
        colors = [
            (self.convert_to_hex(item), (item[0], item[1], item[2]))
            for row in img_ndarray
            for item in row
        ]

        hex_colors = [color[0] for color in colors]
        top_colors = self.find_top_colors(hex_colors)
        return top_colors

    def convert_to_hex(self, rgb_list: List[int]):
        r, g, b = rgb_list
        hex_code = f"#{r:02X}{g:02X}{b:02X}"
        return hex_code

    def find_top_colors(self, hex_array: List[str]):

        # return unique values and counts of corresponding values
        values, counts = np.unique(hex_array, return_counts=True)

        # sort counts and return values in descending order
        sorted_indices = np.argsort(counts)[::-1]
        sorted_values = values[sorted_indices]
        # sorted_counts = counts[sorted_indices]
        # print(f"sorted_counts: {sorted_counts[:10]}")

        # TODO: 2. calculated euclidean distance between colors and shrink array
        # based on a delta value doing this manually using euclidean distance maybe
        # somewhat similar to data aggregation using something like k means
        # clustering and would require/benefit using some library that can do that
        # directly instead of having to code it out in numpy

        # return top 10 sorted values
        return sorted_values[:10]


# TODO: 1. make GUI so that:
# a) images can be selected with a file selector ✅
# b) top 10 colors can be displayed in the UI visually alongside the image preview;
# c) delta value for color variance can be input through ui and button to rerun calculations based on new delta
