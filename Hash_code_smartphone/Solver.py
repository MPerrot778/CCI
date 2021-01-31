from typing import *
from Problem import Problem
import numpy as np
import random


class Solver:

    MAX_ARM = 100

    def __init__(self, problem: Problem):
        self.problem = problem
        self.used_map = np.full((problem.width, problem.height), ' ')
        self.arms = []

    def submit(self, output_filename: str):
        pass

    def compute_solution(self):
        step_count = 1
        nbr_arm_created = 0
        arms_tasks = [[] for _ in range(len(self.arms))]
        for arm_id in range(self.problem.robotic_arm_count):
            point = self.problem.mounting_points.pop(random.random() * len(self.problem.mounting_points) - nbr_arm_created)
            self.arms.append(Arm(point, self.problem.game_map))

        while step_count <= self.problem.step_count:
            for i, arm in enumerate(self.arms):
                if len(arms_tasks[i]) > 0:
                    arm.move(arms_tasks[i][0])
                else:
                    if arm.current_position() == arm.mounting_point:
                        arm.retract()
                    else:
                        arms_tasks[i].extend(self.next_task(arm.current_position(),self.problem.task_list))
                        arm.move(arms_tasks[i][0])

            step_count += 1

    def next_task(self, actual_position, task_list):
        return task_list.pop()