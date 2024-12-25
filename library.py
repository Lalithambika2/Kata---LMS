# KATA - Library Management System

# Main implementation file
class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publication_year):
        if isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        book = Book(isbn, title, author, publication_year)
        self.books[isbn] = book

    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if not book.is_available:
            raise ValueError("Book is currently not available.")
        book.is_available = False

    def return_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if book.is_available:
            raise ValueError("Book was not borrowed.")
        book.is_available = True

    def view_available_books(self):
        return [book for book in self.books.values() if book.is_available]

