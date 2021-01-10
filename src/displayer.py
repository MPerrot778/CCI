from src.image_map import ImageMap
import matplotlib.pyplot as pyplot
import numpy as np


class Displayer:
    def __init__(self):
        self.figure = pyplot.figure()
        self.figure.show()

    def display_game_map(self, image_map: ImageMap):
        """
        MatPlotLib Reference: https://matplotlib.org/3.1.0/gallery/mplot3d/voxels.html
        :param image_map:
        :return:
        """

        size = image_map.get_imageSize()
        blocks = np.full((size, size, size), False, dtype=bool)
        block_colors = np.full((size, size, size), 0, dtype=object)

        self.figure.clear()
        axes = self.figure.gca(projection='3d')

        for x in range(size):
            for y in range(size):
                for z in range(size):
                    block_color = image_map.get_pixelColor((x, y, z))
                    if block_color is not None and len(block_color) == 3:
                        blocks[x, y, z] = True
                        block_colors[x, y, z] = np.array(block_color) / 255

        axes.voxels(blocks, facecolors=block_colors, edgecolors='black')
        self.figure.canvas.draw()

        # Give a break to the CPU
        pyplot.pause(0.1)

    def stop(self):
        """
        Leaves the current plot displayed. Must be called at the end of calls to
        display_game_map. Otherwise, the window will close automatically.
        :return:
        """
        pyplot.show()
