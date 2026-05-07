class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        return None
    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False
    def find_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    def find_by_title(self, title):
        result = []
        for book in self.books:
            if title in book.title:
                result.append(book)
        return result
    def get_all_books(self):
        return self.books
    def get_unread_books(self):
        result = []
        for book in self.books:
            if not book.is_read:
                result.append(book)
        return result
    def mark_book_as_read(self, book_id):
        for book in self.books:
            if book.id == book_id:
                book.mark_as_read()
                return True
        return False
    def get_next_id(self):
        maxx = 0
        for book in self.books:
            if book.id > maxx:
                maxx = book.id
        return maxx + 1