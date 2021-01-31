from typing import *
from collections import deque
import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder
import math


class Arm:
    def __init__(self, mounting_point: Tuple[int, int], used_map: np.ndarray):
        self.moves: List[str] = []
        self.mounting_point = mounting_point
        self.tail = deque([mounting_point])
        self.used_map = used_map
        self.actions = []
        self.__finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

    def move(self, goal_position: Tuple[int, int]):
        pass

    def get_path_to_position(self, goal_position: Tuple[int, int]) -> List[Tuple[int, int]]:
        grid = Grid(matrix=self.used_map, inverse=True)
        start = grid.node(self.current_position[1], self.current_position[0])
        end = grid.node(goal_position[1], goal_position[0])
        path, runs = self.__finder.find_path(start, end, grid)
        return path

    def get_next_position(self, goal_position: Tuple[int, int]) -> Tuple[int, int]:
        return self.get_path_to_position(goal_position)[1]

    def get_closest_position(self, positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        min_distance = math.inf
        best_position = None
        for position in positions:
            distance = self.get_distance(position)
            if distance < min_distance:
                min_distance = distance
                best_position = position
        return best_position

    def get_distance(self, goal_position: Tuple[int, int]) -> int:
        return len(self.get_path_to_position(goal_position)) - 1

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

