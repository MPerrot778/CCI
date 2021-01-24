from Problem import *

class Solver :
    def __init__(self, problem: Problem):
        self.A = 0 # the number of libraries to sign up
        self.lib_read = [] # list of output library
        self.problem = problem
        self.books_read = {}
        self.days_left = problem.D
        pass

    def get_solution(self):
        while self.days_left > 0:
            best_score = 1
            best_lib = None
            for lib in self.problem.Libraries:
                temp_score = self.get_library_score(lib.library_id)
                if best_score < temp_score:
                    best_score = temp_score
                    best_lib = lib
            if best_lib is None:
                break
            book_to_read = []
            book_not_read = [x for element in best_lib.books_sorted_by_score if element not in self.books_read]
            days_left_to_read = self.days_left - best_lib.T
            for i in range(days_left_to_read):
                for j in range(best_lib.M):
                    if len(book_not_read) != 0:
                        temp_book = book_not_read.pop()
                        book_to_read.append(temp_book)
                        self.books_read.add(temp_book)
            self.lib_read.append((best_lib.library_id, len(book_to_read), book_to_read))
            self.A += 1
            self.days_left += - best_lib.T       


    def write_solution(self, outName):
        pass
    
    
    def get_library_score(self, library_id):
        pass
