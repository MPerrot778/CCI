from Problem import Problem
from Solver import Solver
import os


if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.realpath(__file__))
    problem = Problem.get_from_file(os.path.join(current_directory, "example_files", "c_few_arms.txt"))
    solver = Solver(problem)
    solver.compute_solution()
    solver.submit("c_solution.txt")
