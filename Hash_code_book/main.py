from Hash_code_book.Problem import Problem
from Hash_code_book.Solver import Solver

if __name__ == '__main__':
    PA = Problem("problems/a_example.txt")
    PA.read()

    solver = Solver(PA)
    solver.get_solution()
    print(solver.lib_read)
