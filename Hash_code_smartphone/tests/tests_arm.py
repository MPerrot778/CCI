import unittest
from Arm import Arm
import numpy as np
import math
from constants import *


class MyTestCase(unittest.TestCase):
    def test_get_next_position_1(self):
        used_map = np.array([
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        arm = Arm((0, 1), used_map)
        self.assertEqual(arm.get_next_position((0, 3)), (1, 1))
        self.assertEqual(arm.get_distance((0, 3)), 6)

    def test_get_next_position_2(self):
        used_map = np.array([
            [1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1]
        ])
        arm = Arm((0, 1), used_map)
        self.assertEqual(arm.get_next_position((0, 4)), (1, 1))
        self.assertEqual(arm.get_distance((0, 4)), 9)
        self.assertEqual(arm.get_path_to_position((0, 4)), [
            (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4)
        ])

    def test_get_next_position_no_path(self):
        used_map = np.array([
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ])
        arm = Arm((0, 1), used_map)
        self.assertEqual(arm.get_next_position((0, 3)), (0, 1))
        self.assertEqual(arm.get_distance((0, 3)), INFINITY_INT)

if __name__ == '__main__':
    unittest.main()
