from Solver import Solver
from Problem import Problem
import unittest


class MyTestCase(unittest.TestCase):

    def test_get_score_0(self):
        rides = [(5,6,9,2,3,10),(0,0,2,2,0,4),(0,0,9,9,4,22),(1,3,3,3,2,10),(5,5,9,0,0,45)]
        prob0 = Problem(10,10,3,len(rides),5,100,rides)
        solv = Solver(prob0)

        score,ride_score,nb_steps = solv.get_score(0,(0,0),solv.problem.rides[1])
        self.assertEqual(score,9)
        self.assertEqual(ride_score,9)
        self.assertEqual(nb_steps,4)
