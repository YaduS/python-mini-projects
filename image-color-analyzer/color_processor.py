from PIL import ImageFile
import numpy as np
from scipy.spatial import distance

from typing import List

DEFAULT_COLOR_DELTA = 30


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
        img_ndarray = np.array(self.img)
        height, width, _ = img_ndarray.shape
        print(f"resolution: {width} x {height}")
        colors = [
            (self.rgb_to_hex(item), (int(item[0]), int(item[1]), int(item[2])))
            for row in img_ndarray
            for item in row
        ]

        top10_colors = self.sort_and_merge_colors(colors)

        return top10_colors

    def sort_and_merge_colors(self, colors):

        hex_colors, rgb_colors = zip(*colors)
        hex_colors, rgb_colors = list(hex_colors), list(rgb_colors)
        top10_changed = True

        # here its not unique yet..
        unique_colors = hex_colors
        while top10_changed:

            colors, counts = np.unique(unique_colors, return_counts=True)
            sorted_indices = np.argsort(counts)[::-1]
            sorted_colors = colors[sorted_indices].tolist()
            top10_colors = sorted_colors[:10]

            top10_changed = False
            for i, top_color in enumerate(top10_colors):
                for j in range(i + 1, len(sorted_colors)):
                    rgb_color = self.hex_to_rgb(sorted_colors[j])
                    rgb_top_color = self.hex_to_rgb(top_color)

                    dis = distance.euclidean(rgb_color, rgb_top_color)

                    if dis < self.delta and sorted_colors[j] != top_color:
                        # print(dis)
                        sorted_colors[j] = top_color
                        top10_changed = True

                if top10_changed:
                    print(
                        f"changed top10_color: {top_color} count; jumping out to resort again"
                    )
                    unique_colors = sorted_colors
                    break

        return top10_colors

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb_list: List[int]):
        r, g, b = rgb_list
        hex_code = f"#{r:02X}{g:02X}{b:02X}"
        return hex_code

    def find_top_colors(self, hex_array: List[str]):
        values, counts = np.unique(hex_array, return_counts=True)
        sorted_indices = np.argsort(counts)[::-1]
        sorted_values = values[sorted_indices]

        return sorted_values[:10]
