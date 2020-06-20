# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:14:37 2019

@author: Supi
"""


class Book:
    """
    class represent a Book
    """

    def __init__(self):
        self.isbn = 0
        self.bookName = ""
        self.user = None
        self.damageDescriptions = []

        """
        data fields attributes for the class Book 
        """

    def setIsbn(self, isbn):
        self.isbn = isbn

    """
    set method to set the isbn for the book
    """

    def getIsbn(self):
        return self.isbn

    def setBookName(self, bookName):
        self.bookName = bookName

    """
    set method to set the book name
    """

    def getBookName(self):
        return self.bookName

    """
    get method to get the book name
    """

    def setUser(self, user):
        self.user = user

        """
        setter method to set the user 
        """

    def getUser(self):
        return self.user

    """
    getter method to get the user
    """

    def getDamageDescriptions(self):
        return self.damageDescriptions

    """
    getter method to get the description of the damage of the book
    """

    def addDamageDescription(self, damage):
        self.damageDescriptions.append(damage)

    def isBookAvailable(self, isbn):
        if (self.isbn == isbn):
            if (self.getUser() is None):
                return True
            else:
                return False
        else:
            return False

    """
     A method that checks if a book is available and the returns true if the value of the library
     member data field is None ,Otherwise returns the false.
     """

    def getBookDetailsByIsbn(self, isbn):
        if (self.isbn == isbn):
            if (self.getUser() is None):
                return "Isbn: " + str(
                    self.isbn) + ", Book Name: " + self.bookName + ", Damage Descriptions: " + ",".join(
                    self.damageDescriptions)
            else:
                return "Isbn: " + str(
                    self.isbn) + ", Book Name: " + self.bookName + ", Borrowed By: " + self.user.userName + ", Damage Descriptions: " + ", ".join(
                    self.damageDescriptions)
        else:
            return "Isbn: {} not Found".format(isbn)

    def getBookDetails(self):
        if (self.getUser() is None):
            return "Isbn: " + str(
                self.isbn) + ", Book Name: " + self.bookName + ", Damage Descriptions: " + ",".join(
                self.damageDescriptions)
        else:
            return "Isbn: " + str(
                self.isbn) + ", Book Name: " + self.bookName + ", Borrowed By: " + self.user.userName + ", Damage Descriptions: " + ", ".join(
                self.damageDescriptions)

    """
    A method that prints all the details of a book.
    """
