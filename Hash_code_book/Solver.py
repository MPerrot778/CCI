from Problem import *

class Solver :
    def __init__(self, problem: Problem):
        self.problem = problem
        self.books_read = set()
        self.days_left = problem.D
        pass

    def get_solution(self):
        pass
    
    def write_solution(self, outName):
        pass

    def get_library_score(self, library_id):
        score_de_la_librairie = 0
        if self.days_left > self.problem.Libraries[library_id].T : #On s'assure que le nombre de jours pour le sign_up est plus petit que le nombre de jours restant
            days_of_book_scanning_left: int = self.days_left - self.problem.Libraries[library_id].T
            while days_of_book_scanning_left != 0: #Tant qu'il nous reste des journées de traitement, on continue
                days_of_book_scanning_left -= 1
                number_of_books_scanned_in_parallel = self.problem.Libraries[library_id].M
                books_left_to_be_treated = self.problem.Libraries[library_id].books_sorted_by_score
                #Tant que le nombre de livres à traiter en parallèle et la taille de la liste des livres de la librairie ne sont pas de 0, on continue
                while number_of_books_scanned_in_parallel != 0 and len(books_left_to_be_treated) != 0:
                    id_of_book = books_left_to_be_treated[0]
                    while id_of_book in self.books_read: #Si le livre a déjà été traité, on passe au suivant
                        books_left_to_be_treated.pop(0)
                        id_of_book = books_left_to_be_treated[0]
                    books_left_to_be_treated.pop(0)
                    number_of_books_scanned_in_parallel -= 1
                    score_de_la_librairie += self.problem.get_score(id_of_book)
        return score_de_la_librairie
