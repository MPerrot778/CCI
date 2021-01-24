
class Library : 
    def __init__(self, N, T, M, books):
        self.N = N # the number of books in library
        self.T = T # the number of days it takes to nish the library signup process for library
        self.M = M # the number of books that can be shipped from library j to the scanning facility per day, once the library is signed up.
        self.books_sorted_by_score = sorted(books, reverse=True)


    

