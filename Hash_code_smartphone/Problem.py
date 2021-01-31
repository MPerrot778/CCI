import numpy as np
from typing import *
from Task import Task

class Problem:

    @staticmethod
    def get_from_file(filename: str):

        mounting_point_count = 0
        mounting_points = []

        assembly_points_count = 0
        assembly_points = []

        task_list = []
        task = True

        with open(filename,'r') as f :
            lines = f.readlines()
            row = 0

            for line in lines:
                if(line == '\n'):
                    break
                else :
                    line = line.split(' ')
                    if row == 0:
                        width = int(line[0])
                        height = int(line[1])
                        robotic_arm_count = int(line[2])
                        mounting_point_count = int(line[3])
                        task_count = int(line[4])
                        step_count = int(line[5])

                    elif (row > 0 and row <= mounting_point_count):
                        mounting_points += [(int(line[0]), int(line[1]))]
                    
                    else:
                        if(task):
                            score = int(line[0])
                            assembly_points_count = int(line[1])
                            task = False
                        else:
                            for i in range(assembly_points_count):
                                assembly_points += [(int(line[0 + 2*i]), int(line[1 + 2*i]))]
                            
                            task_list += [Task(score,assembly_points)]
                            assembly_points = []
                            task = True
                row += 1  
            
        return Problem(width, height, robotic_arm_count, mounting_point_count, mounting_points, task_count, task_list, step_count)
        

    def __init__(self, width, height, robotic_arm_count, mounting_point_count, mounting_points,
                 task_count, task_list, step_count):
        self.width = width
        self.height = height
        self.robotic_arm_count = robotic_arm_count
        self.mounting_point_count = mounting_point_count
        self.mounting_points = mounting_points
        self.task_count = task_count
        self.task_list = task_list
        self.step_count = step_count
        self.game_map = np.full((self.width, self.height), ' ')
    

