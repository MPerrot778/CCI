from typing import *

class Task:
    def __init__(self,score: int, assembly_points):
        self.score = score
        self.assembly_points = assembly_points
    
    def __len__(self):
        return len(self.assembly_points)