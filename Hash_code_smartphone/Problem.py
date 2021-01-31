import numpy as np


class Problem:

    @staticmethod
    def get_from_file(filename: str):
        pass

    def __init__(self, width, height, robotic_arm_count, mounting_point_count,
                 task_count, step_count):
        self.width = 0
        self.height = 0
        self.robotic_arm_count = 0
        self.mounting_point_count = 0
        self.task_count = 0
        self.step_count = 0
        self.game_map = np.full((self.width, self.height), ' ')
