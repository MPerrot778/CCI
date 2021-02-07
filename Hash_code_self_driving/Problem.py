class Problem:
    @staticmethod
    def get_from_file(filename: str):
        pass

    def __init__(self):
        self.R = 0
        self.C = 0
        self.F = 0
        self.N = 0
        self.B = 0
        self.T = 0

        self.rides = [] # [(a, b, x, y, s, f)]
