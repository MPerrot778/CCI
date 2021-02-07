from Problem import Problem
from Solver import Solver

if __name__ == '__main__':
    problem_names = [
        "a_example",
        "b_should_be_easy",
        "c_no_hurry",
        "d_metropolis",
        "e_high_bonus"
    ]
    for problem_name in problem_names:
        problem = Problem.get_from_file(f"Problems/{problem_name}.in")
        solver = Solver(problem)
        solver.solve()

        print(f"Problem {problem_name}")
        print(solver.vehicule_rides)
        print("score", solver.total_score)
        solver.submit(f"Solutions/{problem_name}.out")
