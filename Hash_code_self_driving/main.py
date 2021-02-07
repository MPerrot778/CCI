from Problem import Problem
from Solver import Solver

if __name__ == '__main__':
    problem = Problem.get_from_file("Problems/a_example.in")
    solver = Solver(problem)
    solver.solve()
    print(solver.vehicule_rides)
