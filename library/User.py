# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:53:35 2019

@author: Supi
"""


class User:
    """
      class represent a User
     """

    def __init__(self):
        self.userId = 0
        self.userName = "not set"
        self.booksBorrowed = []
        self.messages = []
        """
        data fields attributes for the class EDevice
       """

    def setUserId(self, Id):
        self.userId = Id

    def getUserId(self):
        return self.userId

    def setUserName(self, name):
        self.userName = name

    def getUserName(self):
        return self.userName

    def setBooksBorrowed(self, book):
        self.booksBorrowed.append(book)

    def getBooksBorrowed(self):
        return self.booksBorrowed

    """
    all the set and get method to set and get the value of the attributes of the class User
    """

    def addMessage(self, message):
        self.messages.append(message)

    """
    method to add the message using append and passing the message parameter with the self instance 
    """

    def getAllMessagesByUserId(self, userId):
        if (self.userId == userId):
            return "User Id: " + str(self.userId) + ", User Name: " + self.userName + ", Messages: " + ", ".join(
                self.messages)
        else:
            return "User Id: {} not Found".format(userId)

    """
    method to find all the deatils of the user using the if else condition.
    """

    def getAllBooksByUserId(self, userId):
        if self.userId == userId:
            bookDetails = " "
            if len(self.booksBorrowed) > 0:
                for book in self.booksBorrowed:
                    bookDetails += book.getBookDetailsByIsbn(book.getIsbn())
            return "User Id: " + str(self.userId) + ", User Name: " + self.userName + ", Books borrowed: " + bookDetails
        else:
            return "User Id: {} not Found".format(userId)

    """
    method to get all the bookdetails by passing the userId parameter with concatenate 
    """

    def getBooksBorrowedCount(self, userId):
        if self.userId == userId:
            return "User Id: {} has borrowed {} books".format(userId, len(self.booksBorrowed))
        else:
            return "User Id: {} not Found".format(userId)

    """
    method to get all the details of the borrowed book and the user
    """
