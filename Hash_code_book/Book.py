class Book :
    def __init__(self, book_id, book_score):
        self.book_id = book_id
        self.book_score = book_score

    def __lt__(self, other):
        return self.book_score < other.book_score
    
    def __le__(self, other):
        return self.book_score <= other.book_score

    def __gt__(self, other):
        return self.book_score > other.book_score

    def __ge__(self, other):
        return self.book_score >= other.book_score

    def __repr__(self):
        return "Book " + str(self.book_id) + " with a score of " + str(self.book_score)
