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

    def __str__(self):
        return "Book " + self.book_id + " with a score of " + self.book_score
