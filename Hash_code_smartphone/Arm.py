from typing import *

class Arm:
    def __init__(self, mounting_point: Tuple[int]):
        self.moves: List[str] = []
        self.tasks: List[int] = []
        self.mounting_point = mounting_point

    def move(self, action: str):
        pass

    def get_possible_moves(self) -> List[str]:
        pass

