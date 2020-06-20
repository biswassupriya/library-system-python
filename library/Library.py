# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:53:35 2019

@author: Supi
"""
from library.Book import Book
from library.EResource import EResource


class Library:
    """
      class represent a User
     """

    def __init__(self):
        self.resourceCatalog = []
        """
        data fields attributes for the class EDevice
       """

    def getResourceCatalogDetails(self):
        resourceCatalogDetails = ""
        for resource in self.resourceCatalog:
            if (isinstance(resource, EResource)):
                eResource = type(resource)
                resourceCatalogDetails += eResource.getEResourceDetails()
            if (isinstance(resource, Book)):
                book = type(resource)
                resourceCatalogDetails += book.getBookDetails()
        return resourceCatalogDetails

    def isResourceInResourceCatalog(self, resourceObj):
        resourceFound = False
        eResourceObj = None
        bookObj = None
        if (isinstance(resourceObj, EResource)):
            eResourceObj = type(resourceObj)
        if (isinstance(resourceObj, Book)):
            bookObj = type(resourceObj)
        for resource in self.resourceCatalog:
            if (isinstance(resource, EResource)):
                eResource = type(resource)
                if eResource.getEResourceId == eResourceObj.getEResourceId:
                    resourceFound = True
                    break
            if (isinstance(resource, Book)):
                book = type(resource)
                if book.getIsbn() == bookObj.getIsbn():
                    resourceFound = True
                    break
        return resourceFound

    """
    method that checks if the catalogue contains a resource. The method accepts a
    parameter, i.e. the resource object. It returns true if the resource is contained in
    the catalogue. Otherwise, it returns false.

    """

    def getResourceFromResourceCatalog(self, resourceObj):
        eResourceObj = None
        bookObj = None
        responseResource = None
        if (isinstance(resourceObj, EResource)):
            eResourceObj = type(resourceObj)
        if (isinstance(resourceObj, Book)):
            bookObj = type(resourceObj)
        for resource in self.resourceCatalog:
            if (isinstance(resource, EResource)):
                eResource = type(resource)
                if eResource.getEResourceId == eResourceObj.getEResourceId:
                    responseResource = eResource
                    break
            if (isinstance(resource, Book)):
                book = type(resource)
                if book.getIsbn() == bookObj.getIsbn():
                    responseResource = book
                    break
        return responseResource

    """
    method that searches the catalogue by resource object. The method accepts a
    parameter, i.e. the resource object. It returns the resource object if the resource
    is contained in the catalogue. Otherwise, it returns None
    """

    def removeResourceFromResourceCatalogByResource(self, resourceObj):
        responseResource = self.getResourceFromResourceCatalog(resourceObj)
        if responseResource is not None:
            self.resourceCatalog.remove(resourceObj)
            return "Resource Deleted"
        else:
            return "Resource Not Found"

    """
     method that removes a resource from the library catalogue. The method
     accepts a parameter, i.e. the resource object to remove but if the resource is
     not in the catalogue then it returns Resource not found
    """

    def removeResourceFromResourceCatalogByResourcePosition(self, position):
        if len(self.resourceCatalog) >= position:
            del self.resourceCatalog[position]
            return "Resource Deleted"
        else:
            return "position does Not exist"

    """
    method that removes a resource at a specific position in the library catalogue.
    Similar to the previous method, but the parameter represents a position in the
    catalogue
    """

    def getResourceCatalogCount(self):
        return len(self.resourceCatalog)

    """
    returns the number of resources in the library catalogue
    """

    def addResourceToResourceCatlog(self, resourceObj):
        if self.isResourceInResourceCatalog(resourceObj):
            self.resourceCatalog.append(resourceObj)
            return "Resource Already exists"
        else:
            return "Resource Added"

    """
    method that simulates adding a resource to the catalogue. The method accepts
    an object as a parameter and appends this object at the end of the library
    catalogue. If the object already exists in the catalogue, the method should reject
    it and print an appropriate error message
    """


def getResourceCatalogBookDetails(self):
    resourceCatalogBookDetails = ""
    for resource in self.resourceCatalog:
        if (isinstance(resource, EResource)):
            continue
        if (isinstance(resource, Book)):
            book = type(resource)
            resourceCatalogBookDetails += book.getBookDetails()
    return resourceCatalogBookDetails


"""
method that prints the details of all book resources in the catalogue.
"""


def getResourceCatalogEResourceDetails(self):
    resourceCatalogEResourceDetails = ""
    for resource in self.resourceCatalog:
        if (isinstance(resource, EResource)):
            eResource = type(resource)
            resourceCatalogEResourceDetails += eResource.getEResourceDetails()
        if (isinstance(resource, Book)):
            continue
    return resourceCatalogEResourceDetails


"""
method that prints the details of all electronic resources in the catalogue
"""
