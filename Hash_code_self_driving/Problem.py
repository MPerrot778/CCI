class Problem:
    @staticmethod
    def get_from_file(filename: str):
        with open(filename, 'r') as file:
            first_line = file.readline().split()
            number_of_rows = int(first_line[0])
            number_of_columns = int(first_line[1])
            number_of_vehicules_in_fleet = int(first_line[2])
            number_of_rides = int(first_line[3])
            bonus = int(first_line[4])
            number_of_steps = int(first_line[5])
            rides = [] #Contient toutes les rides et leurs valeurs associées
            for line in file.readlines():
                if (line != '\n'):
                    line = line.split(' ')
                    a = int(line[0])
                    b = int(line[1])
                    x = int(line[2])
                    y = int(line[3])
                    s = int(line[4])
                    f = int(line[5])
                    rides += [(a, b, x, y, s, f)]
        return Problem(number_of_rows,number_of_columns,number_of_vehicules_in_fleet,number_of_rides,bonus,number_of_steps,rides)




    def __init__(self,number_of_rows,number_of_columns,number_of_vehicules_in_fleet,number_of_rides,bonus,number_of_steps,rides):
        self.R = number_of_rows
        self.C = number_of_columns
        self.F = number_of_vehicules_in_fleet
        self.N = number_of_rides
        self.B = bonus
        self.T = number_of_steps

        self.rides = rides #[(a, b, x, y, s, f)]