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

# test_library.py (Test file for TDD)
import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("1234", "Book Title", "Author Name", 2023)
        self.assertEqual(len(self.library.books), 1)
        self.assertIn("1234", self.library.books)

    def test_borrow_book(self):
        self.library.add_book("1234", "Book Title", "Author Name", 2023)
        self.library.borrow_book("1234")
        self.assertFalse(self.library.books["1234"].is_available)

    def test_borrow_book_not_available(self):
        self.library.add_book("1234", "Book Title", "Author Name", 2023)
        self.library.borrow_book("1234")
        with self.assertRaises(ValueError):
            self.library.borrow_book("1234")

    def test_return_book(self):
        self.library.add_book("1234", "Book Title", "Author Name", 2023)
        self.library.borrow_book("1234")
        self.library.return_book("1234")
        self.assertTrue(self.library.books["1234"].is_available)

    def test_return_book_not_borrowed(self):
        self.library.add_book("1234", "Book Title", "Author Name", 2023)
        with self.assertRaises(ValueError):
            self.library.return_book("1234")

    def test_view_available_books(self):
        self.library.add_book("1234", "Book Title", "Author Name", 2023)
        self.library.add_book("5678", "Another Book", "Another Author", 2022)
        self.library.borrow_book("1234")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].isbn, "5678")

if __name__ == "__main__":
    unittest.main()
