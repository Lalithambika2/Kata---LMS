# Test file for TDD

import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book = Book("1234", "Book Title", "Author Name", 2023)
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)
        self.assertIn(book, self.library.books)

    def test_borrow_book(self):
        book = Book("1234", "Book Title", "Author Name", 2023)
        self.library.add_book(book)
        self.library.borrow_book("1234")
        self.assertFalse(book.is_available)

    def test_borrow_book_not_available(self):
        book = Book("1234", "Book Title", "Author Name", 2023)
        self.library.add_book(book)
        self.library.borrow_book("1234")
        with self.assertRaises(ValueError):
            self.library.borrow_book("1234")

    def test_return_book(self):
        book = Book("1234", "Book Title", "Author Name", 2023)
        self.library.add_book(book)
        self.library.borrow_book("1234")
        self.library.return_book(book)
        self.assertTrue(book.is_available)

    def test_return_book_not_borrowed(self):
        book = Book("1234", "Book Title", "Author Name", 2023)
        self.library.add_book(book)
        with self.assertRaises(ValueError):
            self.library.return_book(book)

    def test_view_available_books(self):
        book1 = Book("1234", "Book Title", "Author Name", 2023)
        book2 = Book("5678", "Another Book", "Another Author", 2022)
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.borrow_book("1234")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].isbn, "5678")

if __name__ == "__main__":
    unittest.main()
