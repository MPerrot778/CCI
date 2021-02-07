from typing import *


class Solver:
    def __init__(self, problem):
        self.problem = problem
        self.vehicule_rides = None

    def get_distance(self, a: Tuple, b: Tuple) -> int:
        distance = abs(a[0] - b[0]) + abs(a[1]-b[1])
        return distance

    def get_score(self, current_step, start_position: Tuple, ride: Tuple) -> Tuple:
        score = 0

        distance_from_ride = self.get_distance(start_position, (ride[0], ride[1]))
        if current_step + distance_from_ride < ride[4]:
            score += self.problem.B

        ride_duration = self.get_distance((ride[0], ride[1]), (ride[2], ride[3])) + ride[4]
        if(current_step + ride_duration) > ride[5]:
            return None, 0

        score += ride_duration
        score -= distance_from_ride
        nb_steps = distance_from_ride+ride_duration

        return score, nb_steps

    def solve(self):
        remaining_ride_ids = set((r for r in range(len(self.problem.rides))))
        self.vehicule_rides = []

        for vehicule_id in range(self.problem.F):
            current_step = 0
            current_position = (0, 0)
            self.vehicule_rides.append([])

            while current_step < self.problem.T and len(remaining_ride_ids) > 0:
                best_score = -1000000
                best_ride_id = None
                best_steps = None
                for ride_id in remaining_ride_ids:
                    score, steps = self.get_score(current_step, current_position, self.problem.rides[ride_id])
                    if score is not None and score > best_score:
                        best_score = score
                        best_steps = steps
                        best_ride_id = ride_id

                if best_ride_id is None:
                    break
                best_ride = self.problem.rides[best_ride_id]
                current_step += best_steps
                current_position = (best_ride[2], best_ride[3])
                remaining_ride_ids.remove(best_ride_id)
                self.vehicule_rides[vehicule_id].append(best_ride_id)


    def submit(self, file_name):
        f = open(file_name,'w')
        for i in range(self.problem.F):
            f.write("%d " % len(self.vehicule_rides[i]))
            f.writelines(["%d\n" % item  for item in self.vehicule_rides[i]])
        f.close()

