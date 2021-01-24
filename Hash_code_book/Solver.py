from Hash_code_book.Problem import *
from copy import deepcopy


class Solver :
    def __init__(self, problem: Problem):
        self.A = 0 # the number of libraries to sign up
        self.lib_read = [] # list of output library
        self.problem = problem
        self.books_read = set()
        self.days_left = problem.D
        pass

    def get_solution(self):
        while self.days_left > 0:
            best_score = 1
            best_lib = None
            for lib in self.problem.libraries:
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
            self.lib_read.append((best_lib.library_id, len(book_to_read), book_to_read))
            self.A += 1
            self.days_left += - best_lib.T       


    def write_solution(self, outName):
        pass
    
    
    def get_library_score(self, library_id):
        score_de_la_librairie = 0
        if self.days_left > self.problem.libraries[library_id].T: #On s'assure que le nombre de jours pour le sign_up est plus petit que le nombre de jours restant
            days_of_book_scanning_left = self.days_left - self.problem.libraries[library_id].T
            books_left_to_be_treated = deepcopy(self.problem.libraries[library_id].books_sorted_by_score)
            while days_of_book_scanning_left != 0: #Tant qu'il nous reste des journées de traitement, on continue
                days_of_book_scanning_left -= 1
                number_of_books_scanned_in_parallel = self.problem.libraries[library_id].M
                #Tant que le nombre de livres à traiter en parallèle et la taille de la liste des livres de la librairie ne sont pas de 0, on continue
                while number_of_books_scanned_in_parallel != 0 and len(books_left_to_be_treated) != 0:
                    id_of_book = books_left_to_be_treated[0].book_id
                    book_score = books_left_to_be_treated[0].book_score
                    if not (id_of_book in self.books_read):
                        number_of_books_scanned_in_parallel -= 1
                        score_de_la_librairie += book_score
                    books_left_to_be_treated.pop(0)
        return score_de_la_librairie
