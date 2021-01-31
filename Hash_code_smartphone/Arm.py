from typing import *
from collections import deque
import numpy as np


class Arm:
    def __init__(self, mounting_point: Tuple[int], used_map: np.ndarray):
        self.moves: List[str] = []
        self.mounting_point = mounting_point
        self.tail = deque([mounting_point])
        self.used_map = used_map
        self.actions = []

    def move(self, goal_position: Tuple[int]):
        pass

    def get_next_position(self, goal_position: Tuple[int]) -> Tuple[int]:
        pass

    def get_distance(self, goal_position: Tuple[int]) -> int:
        pass

    def retract(self):
        last_position = self.current_position
        self.tail.pop()
        new_position = self.current_position
        if new_position[0] > last_position[0]:
            action = 'R'
        elif new_position[0] < last_position[0]:
            action = 'L'
        elif new_position[1] > last_position[1]:
            action = 'U'
        else:
            action = 'D'
        self.actions.append(action)

    @property
    def current_position(self):
        return self.tail[-1]

    # def get_possible_moves(self) -> List[str]:
    #     pass

