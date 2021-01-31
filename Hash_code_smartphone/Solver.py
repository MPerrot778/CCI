from typing import *
from Problem import Problem
from Arm import Arm
import numpy as np
import random


class Solver:

    MAX_ARM = 100

    def __init__(self, problem: Problem):
        self.problem = problem
        self.used_map = np.full((problem.width, problem.height), ' ')
        self.arms = []

    def submit(self, output_filename: str):
        f = open(output_filename, 'w')
        f.write("%d\n" % len(self.arms))

        for _, arm in enumerate(self.arms):
            f.write("%d %d %d %d\n" % (arm.mounting_point[0], arm.mounting_point[1], len(arm.task_ids), len(arm.actions)))
            for _, ids in enumerate(arm.task_ids):
                f.write("%d " % ids)
            f.write("\n")

            for _, move in enumerate(arm.actions):
                f.write("%s " % move)
            f.write("\n")
        f.close()


    def compute_solution(self):
        step_count = 1
        nbr_arm_created = 0

        for arm_id in range(self.problem.robotic_arm_count):
            point = self.problem.mounting_points.pop(int(random.random() * len(self.problem.mounting_points)) - nbr_arm_created)
            self.arms.append(Arm(point, self.problem.game_map))

        arms_tasks = [[] for _ in range(len(self.arms))]

        while step_count <= self.problem.step_count:
            for i, arm in enumerate(self.arms):
                if len(arms_tasks[i]) > 0:
                    arm.move(arms_tasks[i][0])
                    if arm.current_position == arms_tasks[i][0]:
                        arms_tasks[i].pop(0)
                else:
                    if arm.current_position != arm.mounting_point:
                        arm.retract()
                    else:
                        n_task = self.next_task(arm.current_position,self.problem.task_list)
                        arm.task_ids += [n_task.id]
                        arms_tasks[i].extend(n_task.assembly_points)
                        arm.move(arms_tasks[i][0])

            step_count += 1

    def next_task(self, actual_position, task_list):
        return task_list.pop()