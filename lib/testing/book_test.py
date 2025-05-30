import pytest
from lib.book import Book

def test_book_initialization():
    book = Book("1984", "George Orwell", 328)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.page_count == 328

def test_book_page_count_validation():
    book = Book("Test", "Author", 100)
    book.page_count = -5
    assert book.page_count == 100  # Should not change to invalid value
    book.page_count = 200
    assert book.page_count == 200

def test_book_genre_property():
    book = Book("Test", "Author", 100)
    book.genre = "Fiction"
    assert book.genre == "Fiction"
