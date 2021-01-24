from Hash_code_book.Library import Library
from Hash_code_book.Book import Book

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
        B = 0
        L = 0
        D = 0
        with open(self.fileName,'r') as f :
            lines = f.readlines()
            row = 0
            scores = []
            books_type =  []
            books= []
            lib_list = []
            for line in lines:
                if(line == '\n'):
                    break
                else :
                    line = line.split(' ')
                    if row == 0:
                        B = int(line[0])
                        L = int(line[1])
                        D = int(line[2])
                    elif row == 1:
                        for i in range(B):
                            books_type += [Book(i,int(line[i]))]

                    elif row > 1:
                        if(int(row%2) == 0):
                            N = int(line[0])
                            T = int(line[1])
                            M = int(line[2])
                            books = []
                        else:
                            for i in range(len(line)):
                                books += [books_type[int(line[i])]]
                            lib_list += [Library(N,T,M,books)]
                    row += 1
        return B,L,D,lib_list

    


