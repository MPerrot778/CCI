from typing import *
from Problem import Problem
import numpy as np


class Solver:
    def __init__(self, problem: Problem):
        self.problem = problem
        self.used_map = np.full((problem.width, problem.height), ' ')

    def submit(self, output_filename: str):
        pass

    def compute_solution(self):
        pass
