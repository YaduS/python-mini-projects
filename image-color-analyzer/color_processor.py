from PIL import ImageFile
import numpy as np
import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
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
        # TODO: implement delta in calculations
        img_ndarray = np.array(self.img)
        height, width, _ = img_ndarray.shape
        print(f"resolution: {width} x {height}")
        colors = [
            (self.convert_to_hex(item), (item[0], item[1], item[2]))
            for row in img_ndarray
            for item in row
        ]
        hex_colors = [color[0] for color in colors]
        print(f"hex_colors len: {len(hex_colors)}")
        top_colors = self.find_top_colors(hex_colors)
        return top_colors

    def convert_to_hex(self, rgb_list: List[int]):
        r, g, b = rgb_list
        hex_code = f"#{r:02X}{g:02X}{b:02X}"
        return hex_code

    def cluster_colors(self, sorted_values, sorted_counts):
        print("values", sorted_values[0])
        print("counts", sorted_counts[0])

    def find_top_colors(self, hex_array: List[str]):
        values, counts = np.unique(hex_array, return_counts=True)

        sorted_indices = np.argsort(counts)[::-1]
        sorted_values = values[sorted_indices]
        sorted_counts = counts[sorted_indices]
        self.cluster_colors(sorted_values, sorted_counts)
        return sorted_values[:10]

    def analyze_image_clustered(self, delta=DEFAULT_COLOR_DELTA):
        img_ndarray = np.array(self.img)
        # Reshape and sample the image data
        pixels = img_ndarray.reshape(-1, 3)
        print(f"pixels.shape: {pixels.shape}")
        pixels = shuffle(pixels, n_samples=10000)  # Sample for speed

        # Perform K-means clustering
        kmeans = KMeans(n_clusters=100)
        kmeans.fit(pixels)

        # Get cluster centers and sizes
        colors = kmeans.cluster_centers_
        labels = kmeans.labels_
        counts = np.bincount(labels)

        # Merge similar colors
        merged_colors = []
        merged_counts = []

        for color, count in zip(colors, counts):
            for i, merged in enumerate(merged_colors):
                if distance.euclidean(color, merged) < delta:
                    merged_colors[i] = (
                        merged_colors[i] * merged_counts[i] + color * count
                    ) / (merged_counts[i] + count)
                    merged_counts[i] += count
                    break
            else:
                merged_colors.append(color)
                merged_counts.append(count)

        # Sort by count and get top 10
        sorted_colors = sorted(
            zip(merged_colors, merged_counts), key=lambda x: x[1], reverse=True
        )[:10]
        sorted_colors = [color.astype(int) for color, _ in sorted_colors]
        sorted_colors = [self.convert_to_hex(color) for color in sorted_colors]

        return sorted_colors


# TODO: 1. make GUI so that:
# a) images can be selected with a file selector ✅
# b) top 10 colors can be displayed in the UI visually alongside the image preview;
# c) delta value for color variance can be input through ui and button to rerun calculations based on new delta
