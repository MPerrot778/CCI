from Problem import Problem
from Solver import Solver

if __name__ == '__main__':
    PA = Problem("problems/a_example.txt")
    PA.read()

    solver = Solver(PA)
    solver.get_solution()
    print(solver.lib_read)
    print(solver.A)
    print(solver.days_left)
    solver.write_solution("a_solution.txt")
