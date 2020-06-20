from unittest import TestCase

from library.EDevice import EDevice


class TestEDevice(TestCase):
    def test_getEDeviceDetailsByEDeviceId_returnsAvailable_whenDeviceCreated(self):
        eDevice = EDevice()
        eDevice.setEDeviceId(123)
        eDevice.setEDeviceLocation("Glasgow")
        eDevice.setEDeviceName("Computer")
        self.assertEqual(eDevice.getEDeviceDetailsByEDeviceId(123),
                         "eDeviceId: 123, eDeviceName: Computer, eDeviceLocation: Glasgow, eDevice Availability: Available")

    def test_getEDeviceDetailsByEDeviceId_returnsNotAvailable_whenEDeviceIsAllocated(self):
        eDevice = EDevice()
        eDevice.setEDeviceId(123)
        eDevice.setEDeviceAvailable(False)
        eDevice.setEDeviceLocation("Glasgow")
        eDevice.setEDeviceName("Computer")
        self.assertEqual(eDevice.getEDeviceDetailsByEDeviceId(123),
                         "eDeviceId: 123, eDeviceName: Computer, eDeviceLocation: Glasgow, eDevice Availability: Not Available")

    def test_getEDeviceDetailsByEDeviceId_returnsEdeviceNotFound_whenDeviceDoesNotMatch(self):
        eDevice = EDevice()
        eDevice.setEDeviceId(123)
        self.assertEqual(eDevice.getEDeviceDetailsByEDeviceId(1234), "eDeviceId: 1234 not Found")
