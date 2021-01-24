import unittest
from Hash_code_book.Problem import Problem
from Hash_code_book.Solver import Solver


class MyTestCase(unittest.TestCase):
    def test_get_days_left(self):
        problem = Problem("problems/a_example.txt")
        solver = Solver(problem)
        self.assertEqual(solver.days_left, 7)

    def test_get_library_score(self):
        problem = Problem("problems/a_example.txt")
        solver = Solver(problem)
        self.assertEqual(solver.get_library_score(0), 17)
        self.assertEqual(solver.get_library_score(1), 14)
        solver.days_left = 6
        self.assertEqual(solver.get_library_score(0), 17)
        self.assertEqual(solver.get_library_score(1), 13)
        solver.days_left = 5
        self.assertEqual(solver.get_library_score(0), 17)
        self.assertEqual(solver.get_library_score(1), 10)
        solver.days_left = 4
        self.assertEqual(solver.get_library_score(0), 16)
        self.assertEqual(solver.get_library_score(1), 6)
        solver.days_left = 3
        self.assertEqual(solver.get_library_score(0), 11)
        self.assertEqual(solver.get_library_score(1), 0)
        solver.days_left = 2
        self.assertEqual(solver.get_library_score(0), 0)
        self.assertEqual(solver.get_library_score(1), 0)
        solver.days_left = 1
        self.assertEqual(solver.get_library_score(0), 0)
        self.assertEqual(solver.get_library_score(1), 0)
        solver.days_left = 0
        self.assertEqual(solver.get_library_score(0), 0)
        self.assertEqual(solver.get_library_score(1), 0)


if __name__ == '__main__':
    unittest.main()
