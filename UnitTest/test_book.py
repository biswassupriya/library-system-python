from unittest import TestCase

from library.Book import Book
from library.User import User


class TestBook(TestCase):
    def testAddDamageDescription_addsDamages(self):
        book = Book()
        book.addDamageDescription("paper missing")
        self.assertEqual(book.getDamageDescriptions()[0], "paper missing")

    def testIsBookAvailable_returnTrue_whenNoUserAssigned(self):
        book = Book()
        book.setIsbn(123)
        self.assertTrue(book.isBookAvailable(123))

    def testIsBookAvailable_returnFalse_whenUserAssigned(self):
        book = Book()
        book.setIsbn(123)
        user = User()
        book.setUser(user)
        self.assertFalse(book.isBookAvailable(123))

    def testIsBookAvailable_returnFalse_whenUserIsAssigned_IsbnNotFound(self):
        book = Book()
        book.setIsbn(1234)
        user = User()
        book.setUser(user)
        self.assertFalse(book.isBookAvailable(123))

    def testGetBookDetailsByIsbn_returnWithUserDetails_ifUserIsSet(self):
        book = Book()
        book.setIsbn(123)
        book.setBookName("Hello Brother")
        book.addDamageDescription("Page 40 is Torn")
        book.addDamageDescription("Page 41 is Torn")
        user = User()
        user.setUserName("apple")
        book.setUser(user)
        self.assertEqual(book.getBookDetailsByIsbn(123),
                         "Isbn: 123, Book Name: Hello Brother, Borrowed By: apple, Damage Descriptions: Page 40 is Torn, Page 41 is Torn")

    def testGetBookDetailsByIsbn_returnWithoutUserDetails_ifUserIsNotSet(self):
        book = Book()
        book.setIsbn(123)
        book.setBookName("Hello Brother")
        book.addDamageDescription("Page 40 is Torn")
        self.assertEqual(book.getBookDetailsByIsbn(123),
                         "Isbn: 123, Book Name: Hello Brother, Damage Descriptions: Page 40 is Torn")

    def testGetBookDetailsByIsbn_returnsIsbnNotFound_ifIsbnDoesNotMatch(self):
        book = Book()
        book.setIsbn(1234)
        self.assertEqual(book.getBookDetailsByIsbn(123), "Isbn: 123 not Found")
