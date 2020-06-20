from unittest import TestCase

from library.EDevice import EDevice
from library.EResource import EResource


class TestEResource(TestCase):

    def test_getEResourceDetailsByEResourceId_returnsResourceDetails(self):
        eResource = EResource()
        eResource.setEResourceId(123)
        eResource.setEResourceName("e-book")
        eDevice = EDevice()
        eDevice.setEDeviceId(567)
        eDevice.setEDeviceName("Computer")
        eResource.addEDevices(eDevice)
        self.assertEqual(eResource.getEResourceDetailsByEResourceId(123),
                         "eResourceId: 123, eResourceName: e-book, eDevices:  eDeviceId: 567, eDeviceName: Computer, eDeviceLocation: , eDevice Availability: Available")

    def test_getEResourceDetailsByEResourceId_returnsResourceNotFound_whenResourceDoesNotMatch(self):
        eResource = EResource()
        eResource.setEResourceId(123)
        eResource.setEResourceName("e-book")
        self.assertEqual(eResource.getEResourceDetailsByEResourceId(1234), "eResourceId: 1234 not Found")
