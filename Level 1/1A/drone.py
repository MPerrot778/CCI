class Drone:
    def __init__(self, game_map_3d, game_map_2d):
        self.game_map_3d = game_map_3d
        self.game_map_2d = game_map_2d
        self.size = len(game_map_2d)
        self.hopper = []
        self.memory = None
        # TODO: find initial position
        self.position = (0, 0, self.size - 1)
        self.last_touched_color = None

    def get_memory(self):
        return self.memory

    def get_hopper(self):
        return self.hopper

    def add_block_to_hopper(self, position, color):
        self.hopper.append(color)
        self.game_map_3d[position[0]][position[1]][position[2]] = None

    def move(self, delta) -> int:
        """

        :param delta: the position change (x,y)
        :return: The time for the move
        """
        pass

    def place(self, color) -> int:
        if self.game_map_3d[self.position[0]][self.position[1]][self.size - 1] is not None:
            raise Exception("Can't place a block there, already full")
        for i, c in enumerate(self.hopper):
            if c == color:
                hopper_index = i
                break
        else:
            raise Exception("Color not found in hopper")

        for z in range(self.size - 1, 0, -1):
            if self.game_map_3d[self.position[0]][self.position[1]][z] is not None:
                self.game_map_3d[self.position[0]][self.position[1]][z + 1] = color
                # TODO: update game_map_2d
                del self.hopper[hopper_index]
                break

        if self.last_touched_color == color:
            time_elapsed = 2
        else:
            time_elapsed = 3
        self.last_touched_color = color
        return time_elapsed
