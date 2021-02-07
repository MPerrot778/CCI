from Problem import Problem
from Solver import Solver

if __name__ == '__main__':
    problem = Problem.get_from_file("Problems/b_should_be_easy.in")
    solver = Solver(problem)
    solver.solve()
    print(solver.vehicule_rides)
    print("score", solver.total_score)
