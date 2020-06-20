from unittest import TestCase

from library.Book import Book
from library.User import User


class TestUser(TestCase):
    def test_getAllMessagesForUserId_returnsUserIdNotFound_whenUserIdDoesNotMatch(self):
        user = User()
        user.setUserId(1234)
        self.assertEqual(user.getAllMessagesByUserId(123), "User Id: 123 not Found")

    def test_getAllMessagesForUserId_returnsNumberOfBooksBoorowed_whenUserIdMatches(self):
        user = User()
        user.setUserId(1234)
        user.setUserName("Gene")
        user.addMessage("Return Book 123")
        user.addMessage("Book 123 should be returned by next week")
        self.assertEqual(user.getAllMessagesByUserId(1234),
                         "User Id: 1234, User Name: Gene, Messages: Return Book 123, Book 123 should be returned by next week")

    def test_getAllBooksByUserId_returnsAllBookDeatils_whenUserIdMatches(self):
        book = Book()
        book.setIsbn(98)
        book.setBookName("Hello Brother")
        book.addDamageDescription("Page 40 is Torn")
        book.addDamageDescription("Page 41 is Torn")
        user = User()
        user.setUserId(123)
        user.setUserName("Gene")
        user.setBooksBorrowed(book)
        self.assertEqual(user.getAllBooksByUserId(123),
                         "User Id: 123, User Name: Gene, Books borrowed:  Isbn: 98, Book Name: Hello Brother, Damage Descriptions: Page 40 is Torn,Page 41 is Torn")

    def test_getBooksBorrowedCount_returnsUserIdNotFound_whenUserIdDoesNotMatch(self):
        user = User()
        user.setUserId(1234)
        self.assertEqual(user.getBooksBorrowedCount(123), "User Id: 123 not Found")

    def test_getBooksBorrowedCount_returnsNumberOfBooksBoorowed_whenUserIdMatches(self):
        user = User()
        user.setUserId(1234)
        book = Book();
        user.setBooksBorrowed(book)
        user.setBooksBorrowed(book)
        self.assertEqual(user.getBooksBorrowedCount(1234), "User Id: 1234 has borrowed 2 books")
