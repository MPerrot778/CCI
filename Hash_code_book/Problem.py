from Library import Library

class Problem :
    def __init__(self,fileName):
        self.fileName = fileName

        self.B = 0
        self.L = 0
        self.D = 0
        self.scores = []
        self.Libraries = [] # list of library

    def read(self):
        # read file and extract attribute of the problem
        with open(self.fileName,'r') as f :
            lines = f.readlines()
            row = 0
            scores =  []
            libID = 0
            for line in lines:
                line = line.split(' ')
                if row == 0:
                    B = int(line[0])
                    L = int(line[1])
                    D = int(line[2])
                    libList = [Library() for i in range(L)]
                elif row == 1:
                    for i in range(B):
                        scores += [int(line[i])]
                elif row > 1:
                    if(row%2)
                    

                row += 1
            
        print(B,L,D,scores)

        return 0

    def get_score(self,bookID):
        return self.scores[bookID]
    


