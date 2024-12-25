# KATA - Library Management System

# Main implementation file

class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    return
                else:
                    raise ValueError("Book is not available")
        raise ValueError("Book with ISBN {} not found".format(isbn))

    def return_book(self, book):
        if not book.is_available:
            book.is_available = True
        else:
            raise ValueError("Book was not borrowed")

    def view_available_books(self):
        return [book for book in self.books if book.is_available]
