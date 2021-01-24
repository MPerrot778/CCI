
class Library : 
    def __init__(self,library_id, N, T, M, books):
        self.library_id = library_id
        self.N = N # the number of books in library
        self.T = T # the number of days it takes to nish the library signup process for library
        self.M = M # the number of books that can be shipped from library j to the scanning facility per day, once the library is signed up.
        self.books_sorted_by_score = sorted(books, reverse=True)

    def __str__(self):
        out = f"library id: {self.library_id}\n"
        out += f"library signup time: {self.T}\n"
        out += f"number of books that can be scanned daily: {self.M}\n"
        out += f"books sorted by score: {self.books_sorted_by_score}\n"

        return out

    

