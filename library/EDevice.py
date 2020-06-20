# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:14:37 2019

@author: Supi
"""


class EDevice:
    """
    class represent a Eletronic Device
    """

    def __init__(self):
        self.eDeviceId = 0
        self.eDeviceName = ""
        self.eDeviceLocation = ""
        self.eDeviceAvailable = True

        """
        data fields attributes for the class EDevice 
        """

    def setEDeviceId(self, eDeviceId):
        self.eDeviceId = eDeviceId

    def getEDeviceId(self):
        return self.eDeviceId

    def setEDeviceName(self, eDeviceName):
        self.eDeviceName = eDeviceName

    def getEDeviceName(self):
        return self.eDeviceName

    def setEDeviceLocation(self, eDeviceLocation):
        self.eDeviceLocation = eDeviceLocation

    def getEDeviceLocation(self):
        return self.eDeviceLocation

    def setEDeviceAvailable(self, eDeviceAvailable):
        self.eDeviceAvailable = eDeviceAvailable

    """
      set and get method for all the instance variable of the class EDevice
    """

    def isEDeviceAvailable(self, eDeviceId):
        if self.eDeviceId == eDeviceId:
            return self.eDeviceAvailable
        else:
            return False

    """
    method to define if the device is avaiable then to pass the return value else retrun value should be false by using the if else condition
    """

    def getEDeviceDetailsByEDeviceId(self, eDeviceId):
        if self.eDeviceId == eDeviceId:
            return "eDeviceId: " + str(self.getEDeviceId()) + ", eDeviceName: " + self.getEDeviceName() \
                   + ", eDeviceLocation: " + self.getEDeviceLocation() + ", eDevice Availability: " + \
                   ("Not Available", "Available")[self.isEDeviceAvailable(eDeviceId)]
            # "Available" if self.isEDeviceAvailable(eDeviceId) else "Not Available"

        else:
            return "eDeviceId: {} not Found".format(eDeviceId)

    """
    get method to pass and print all the details data of the class EDevice 
    """
