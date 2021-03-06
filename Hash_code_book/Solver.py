from Problem import *
from copy import deepcopy

class Solver :
    def __init__(self, problem: Problem):
        self.A = 0 # the number of libraries to sign up
        self.lib_read = [] # list of output library
        self.problem = problem
        self.books_read = set()
        self.days_left = problem.D
        self.score_tot = 0

    def get_solution(self):
        while self.days_left > 0:
            best_score = 0
            best_lib = None
            for lib in [lib for lib in self.problem.libraries if lib.library_id not in [l[0] for l in self.lib_read]]:
                temp_score = self.get_library_score(lib.library_id)
                if best_score < temp_score:
                    best_score = temp_score
                    best_lib = lib
            if best_lib is None:
                break
            book_to_read = []
            book_not_read = [element for element in best_lib.books_sorted_by_score if element not in self.books_read]
            days_left_to_read = self.days_left - best_lib.T
            for i in range(days_left_to_read):
                for j in range(best_lib.M):
                    if len(book_not_read) != 0:
                        temp_book = book_not_read.pop()
                        book_to_read.append(temp_book)
                        self.books_read.add(temp_book)
                        self.score_tot += temp_book.book_score
            self.lib_read.append((best_lib.library_id, len(book_to_read), book_to_read))
            self.A += 1
            self.days_left -= best_lib.T


    def write_solution(self, outName):

        f = open(outName, 'w')
        f.write("%d\n" % self.A)
        for i in range(self.A):
            f.write("%d %d\n" % (self.lib_read[i][0], self.lib_read[i][1]))
            for j in range(self.lib_read[i][1]):
                f.write("%d " % int(self.lib_read[i][2][j].book_id))
            f.write("\n")
        f.close()
    
    
    def get_library_score(self, library_id):
        score_de_la_librairie = 0
        if self.days_left > self.problem.libraries[library_id].T: #On s'assure que le nombre de jours pour le sign_up est plus petit que le nombre de jours restant
            days_of_book_scanning_left = self.days_left - self.problem.libraries[library_id].T
            scanning_slots_left = days_of_book_scanning_left * self.problem.libraries[library_id].M
            books = self.problem.libraries[library_id].books_sorted_by_score
            book_counter = 0
            while scanning_slots_left > 0 and book_counter < len(books): #Tant qu'il nous reste des journées de traitement, on continue
                #Tant que le nombre de livres à traiter en parallèle et la taille de la liste des livres de la librairie ne sont pas de 0, on continue
                id_of_book = books[book_counter].book_id
                if not (id_of_book in self.books_read):
                    scanning_slots_left -= 1
                    score_de_la_librairie += books[book_counter].book_score
                book_counter += 1

        return score_de_la_librairie
