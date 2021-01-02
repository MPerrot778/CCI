from src.image_map import ImageMap
from math import sqrt

EMPTY_COLOR = ""


class Drone:
    def __init__(self, initial_game_map: ImageMap):
        self.game_map = initial_game_map
        self.size = self.game_map.get_imageSize()
        self.hopper = []
        self.memory: ImageMap = ImageMap.create(self.size)
        # TODO: find initial position
        self.position = (0, 0)
        self.last_touched_color = None

    def get_memory(self) -> ImageMap:
        return self.memory

    def get_hopper(self) -> list:
        return self.hopper

    def get_max_hopper_size(self):
        return sqrt(self.size ** 3) // 2

    def add_block_to_hopper(self, color):
        if self.get_max_hopper_size() >= self.size:
            raise Exception("Hopper is full, can't add block to it!")
        self.hopper.append(color)

    def get_top_color(self):
        color = EMPTY_COLOR
        for z in range(self.size - 1, 0, -1):
            if color != EMPTY_COLOR:
                color = self.__get_pixel_color(z)
                break
        return color

    def add_block_to_memory(self, position, color):
        self.memory.set_pixelColor((position[0], position[1], position[2]), color)

    def move(self, delta) -> int:
        """
        Moves in one direction from 1 and returns the time elapsed.
        :param delta: the position change (x,y)
        :return: The time for the move
        """
        self.position = (self.position[0] + delta[0], self.position[1] + delta[1])
        return 1

    def take(self) -> int:
        """
        Takes a block at the top of the current (x, y) position and adds it to the hopper.
        :return: The time elapsed
        """
        for z in range(self.size - 1, 0, -1):
            if self.__get_pixel_color(z) is not None:
                color = self.__get_pixel_color(z)
                self.add_block_to_hopper(color)
                self.__set_pixel_color(z, None)
                break
        else:
            raise Exception("Can't take block here, no block found")

        if self.last_touched_color == color:
            time_elapsed = 2
        else:
            time_elapsed = 3
        self.last_touched_color = color
        return time_elapsed

    def place(self, color, altitude) -> int:
        """
        Places a block at the current (x,y) position
        :param color: The color of the block
        :param altitude: The desired altitude
        :return: The time elapsed
        """

        # validate the altitude is not under existing blocks
        for z in range(self.size - 1, altitude, -1):
            if self.__get_pixel_color(z) is not None:
                raise Exception("Can't place a block there, already full")

        # find the block color in the hopper
        for i, c in enumerate(self.hopper):
            if c == color:
                hopper_index = i
                break
        else:
            raise Exception("Color not found in hopper")

        del self.hopper[hopper_index]

        if self.last_touched_color == color:
            time_elapsed = 2
        else:
            time_elapsed = 3
        self.last_touched_color = color
        return time_elapsed

    def __get_pixel_color(self, altitude):
        return self.game_map.get_pixelColor((self.position[0], self.position[1], altitude))

    def __set_pixel_color(self, altitude, color):
        self.game_map.set_pixelColor((self.position[0], self.position[1], altitude), color)
