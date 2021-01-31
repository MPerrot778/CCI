from typing import *
from collections import deque
import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder
from constants import *
import math


class Arm:
    def __init__(self, mounting_point: Tuple[int, int], used_map: np.ndarray):
        self.mounting_point = mounting_point
        self.tail = deque([mounting_point])
        self.used_map = used_map
        self.actions: List[str] = []
        self.task_ids = []
        self.__finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

    def move(self, goal_position: Tuple[int, int]):
        next_position = self.get_next_position(goal_position)
        if next_position == self.tail[-1]:
            # Wait
            self.actions.append('W')
        elif next_position == self.tail[-2]:
            self.retract()
        else:
            # Expand arm
            self.used_map[next_position] = 1
            self.actions.append(self.__get_action(next_position))
            self.tail.append(next_position)

    def get_path_to_position(self, goal_position: Tuple[int, int]) -> List[Tuple[int, int]]:
        grid = Grid(matrix=self.used_map, inverse=True)
        start = grid.node(self.current_position[1], self.current_position[0])
        end = grid.node(goal_position[1], goal_position[0])
        path, runs = self.__finder.find_path(start, end, grid)
        return [(x, y) for y, x in path]

    def get_next_position(self, goal_position: Tuple[int, int]) -> Tuple[int, int]:
        path = self.get_path_to_position(goal_position)
        if len(path) <= 1:
            return self.current_position
        else:
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
        path = self.get_path_to_position(goal_position)
        if len(path) == 0:
            return INFINITY_INT
        else:
            return len(path) - 1

    def __get_action(self, new_position):
        last_position = self.current_position
        if new_position[0] > last_position[0]:
            action = 'R'
        elif new_position[0] < last_position[0]:
            action = 'L'
        elif new_position[1] > last_position[1]:
            action = 'U'
        else:
            action = 'D'
        return action

    def retract(self):
        self.used_map[self.current_position] = 0
        self.actions.append(self.__get_action(self.tail[-2]))
        self.tail.pop()

    @property
    def current_position(self):
        return self.tail[-1]
