from typing import *


class Solver:
    def __init__(self, problem):
        self.problem = problem

    def get_distance(self, a: Tuple, b: Tuple) -> int:
        distance = abs(a[0] - b[0]) + abs(a[1]-b[1])
        return distance

    def get_score(self, current_step, start_position: Tuple, ride: Tuple) -> int:
        score = 0

        distance_from_ride = self.get_distance(start_position, (ride[0], ride[1]))
        if current_step + distance_from_ride < ride[4]:
            score += self.problem.B

        ride_duration = self.get_distance((ride[0], ride[1]), (ride[2], ride[3]))
        # TODO: take into consideration arrival time
        if(current_step + ride_duration) > ride[5]:
            return None

        score += ride_duration
        score -= distance_from_ride
        return score

    def solve(self):
        remaining_rides = set(self.problem.rides)
        for vehicule_id in range(self.problem.F):
            for ride in remaining_rides:
                pass


    def submit(self, file_name):
        pass

