# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:14:37 2019

@author: Supi
"""


class EResource:
    """
    class represent a Eletronic Resource
    """

    def __init__(self):
        self.eResourceId = 0
        self.eResourceName = ""
        self.eDevices = []

        """
        data fields attributes for the class EResource
        """

    def setEResourceId(self, eResourceId):
        self.eResourceId = eResourceId

    def getEResourceId(self):
        return self.eResourceId

    def setEResourceName(self, eResourceName):
        self.eResourceName = eResourceName

    def getEResourceName(self):
        return self.eResourceName

    def getEDevices(self):
        return ", ".join(self.eDevices)

    """
     all the get and set method for the data field/variables of the class EResource
    """

    def addEDevices(self, eDevice):
        self.eDevices.append(eDevice)

    """
     method that accepts a device object as a parameter, and appends the object at the end of the device list/array.
    """

    def getEResourceDetailsByEResourceId(self, eResourceId):
        if self.eResourceId == eResourceId:
            eDeviceDetails = " "
            if len(self.eDevices) > 0:
                for eDevice in self.eDevices:
                    eDeviceDetails += eDevice.getEDeviceDetailsByEDeviceId(eDevice.getEDeviceId())
            return "eResourceId: " + str(self.getEResourceId()) + ", eResourceName: " + self.getEResourceName() \
                   + ", eDevices: " + eDeviceDetails

        else:
            return "eResourceId: {} not Found".format(eResourceId)

    """
    print method to get all the deatil of the Eresource class
    """

    def getEResourceDetails(self):
        eDeviceDetails = " "
        if len(self.eDevices) > 0:
            for eDevice in self.eDevices:
                eDeviceDetails += eDevice.getEDeviceDetailsByEDeviceId(eDevice.getEDeviceId())
        return "eResourceId: " + str(self.getEResourceId()) + ", eResourceName: " + self.getEResourceName() \
               + ", eDevices: " + eDeviceDetails
