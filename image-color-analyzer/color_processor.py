from PIL import ImageFile
import numpy as np
from scipy.spatial import distance
from typing import List
from collections import Counter
from time import time

DEFAULT_COLOR_DELTA = 30


class ColorProcessor:

    def __init__(self):
        self.img: ImageFile = None
        self.delta = 1

    def load_image(self, img: ImageFile):
        self.img = img

    def analyze_image(self, delta: int):
        # print(f"analyze start time: {time()}")
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

        color_counts = Counter(rgb_colors).most_common()
        rgb_sorted_color, rgb_count = zip(*color_counts)

        clusters = []

        print(f"no of unique colors: {len(rgb_sorted_color)}")
        # print(f"loop start time: {time()}")
        for i in range(len(rgb_sorted_color)):
            # debug using time
            # if not i % 10000:
            #     print(f"time: {time()}")
            color = rgb_sorted_color[i]
            count = rgb_count[i]
            if not clusters:
                clusters.append({"center": color, "count": count})
            else:
                # if not i % 10000:
                #     print(f"time 1: {time()}")
                nearest = min(
                    clusters, key=lambda c: distance.euclidean(c["center"], color)
                )
                # if not i % 10000:
                #     print(f"time 2: {time()}")
                if distance.euclidean(nearest["center"], color) < self.delta:
                    nearest["count"] += count
                    # for now commenting out taking the weighted average value
                    # total = nearest["count"]
                    # nearest["center"] = tuple(
                    #     (
                    #         np.array(nearest["center"]) * (total - count)
                    #         + np.array(color) * count
                    #     )
                    #     / total
                    # )
                else:
                    clusters.append({"center": color, "count": count})

        sorted_clusters = sorted(clusters, key=lambda c: c["count"], reverse=True)
        print(f"sorted cluster length: {len(sorted_clusters)}")
        top_clusters = sorted_clusters[:10]
        top_colors = [
            self.rgb_to_hex(tuple(map(int, cluster["center"])))
            for cluster in top_clusters
        ]

        print(f"top_clusters: {top_colors}")

        # print(f"color_counts: {color_counts}")
        # print(f"rgb_sorted: {rgb_sorted_color[:10]}")
        # print(f"rbg_counts: {rgb_count[:10]}")

        return top_colors

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
