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
        task_id = 0
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
                            
                            task_list += [Task(score,task_id,assembly_points)]
                            task_id += 1
                            assembly_points = []
                            task = True
                row += 1  
            
        return Problem(width, height, robotic_arm_count, mounting_points, task_list, step_count)
        

    def __init__(self, width, height, robotic_arm_count, mounting_points,
                task_list, step_count):
        self.width = width
        self.height = height
        self.robotic_arm_count = robotic_arm_count
        self.mounting_points = mounting_points
        self.task_list = task_list
        self.step_count = step_count
        self.game_map = self.create_game_map()
    

    def create_game_map(self):
        game_map = np.zeros((self.width, self.height)) # [row][col]

        for i, mounting_point in enumerate(self.mounting_points):
            game_map[mounting_point] = 1

        return game_map   
    
    def get_map_coordinate(self,coordinates):
        return (coordinates[0],self.height - coordinates[1] - 1)

