from Library import Library
from Book import Book

class Problem :
    def __init__(self,fileName):
        self.fileName = fileName

        B,L,D,libraries = self.read()

        self.B = B
        self.L = L
        self.D = D
        self.libraries = libraries

    def read(self):
        # read file and extract attribute of the problem
        with open(self.fileName,'r') as f :
            lines = f.readlines()
            row = 0
            books_type =  []
            books= []
            lib_list = []
            for line in lines:
                line = line.split(' ')
                if row == 0:
                    B = int(line[0])
                    L = int(line[1])
                    D = int(line[2])
                elif row == 1:
                    for i in range(B):
                        books_type += [Book(i,int(line[i]))]
                elif row > 1:
                    if(row%2 == 0):
                        N = int(line[0])
                        T = int(line[1])
                        M = int(line[2])
                    else:
                        for i in range(len(line)):
                            books += [books_type[int(line[i])]]
                        print(books)
                        lib_list += [Library(N,T,M,books)]

                row += 1
        return B,L,D,lib_list

    


