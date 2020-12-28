import image_map

EMPTY_COLOR = ""

class Drone:
    def __init__(self, game_map: image_map):
        self.game_map = game_map
        self.size = len(game_map.scrambled)
        self.hopper = []
        self.memory = ["" for _ in range(self.size) for _ in range(self.size) for _ in range(self.size)]
        # TODO: find initial position
        self.position = (0, 0)
        self.last_touched_color = None

    def get_memory(self):
        return self.memory

    def get_hopper(self):
        return self.hopper

    def get_max_hopper_size(self):
        return len(self.hopper) // 2

    def add_block_to_hopper(self, color):
        if self.get_max_hopper_size() >= self.size:
            raise Exception("Hopper is full, can't add block to it!")
        self.hopper.append(color)

    def get_top_color(self):
        color = EMPTY_COLOR
        for z in range(self.size - 1, 0, -1):
            if color != EMPTY_COLOR:
                color = self.game_map.scrambled[self.position[0]][self.position[1]][z]
                break
        return color

    def add_block_to_memory(self, position, color):
        self.memory[position[0]][position[1]][position[2]] = color

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
        for z in range(size - 1, 0, -1):
            if self.game_map[self.position[0]][self.position[1]][z] is not None:
                color = self.game_map.scrambled[self.position[0]][self.position[1]][z]
                self.add_block_to_hopper(color)
                self.game_map.scrambled[position[0]][position[1]][z] = None
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
        # validate the altitude is not under existing blocks
        for z in range(self.size - 1, altitude, -1):
            if self.game_map[self.position[0]][self.position[1]][z] is not None:
                raise Exception("Can't place a block there, already full")

        # find the block color in the hopper
        for i, c in enumerate(self.hopper):
            if c == color:
                hopper_index = i
                break
        else:
            raise Exception("Color not found in hopper")

        self.game_map.scrambled[self.position[0]][self.position[1]][altitude] = color
        del self.hopper[hopper_index]

        if self.last_touched_color == color:
            time_elapsed = 2
        else:
            time_elapsed = 3
        self.last_touched_color = color
        return time_elapsed
