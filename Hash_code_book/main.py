from Problem import Problem
from Solver import Solver

if __name__ == '__main__':
    PA = Problem("Hash_code_book/problems/d_tough_choices.txt")
    PA.read()

    solver = Solver(PA)
    solver.get_solution()
    solver.write_solution("d_solution.txt")
    print(solver.score_tot)