#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""


TARGET = ('192.168.100.220', 1234, 4)
COMMAND_TYPE = 'ELVA1'
CONNECTION_METHOD = 'GPIB_PROLOGIX'

import pymeasure
import pymeasure.devices
import pymeasure.communicators

import unittest

create_test_device = pymeasure.devices.attenuator
device_under_the_test = pymeasure.devices.dev_attenuator.attenuator

class Test_attenuator(unittest.TestCase):
    def test_initialize(self):
        self.assertIsInstance(create_test_device(COMMAND_TYPE),
                              device_under_the_test)

    def test_set_communicator(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.set_communicator(com),
                              pymeasure.communicators.communicator.communicator)

    def test_get_product_information(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE)
        self.assertIsNotNone(dev.set_communicator(com))
        info = dev.get_product_information()
        print(info)
        self.assertIsInstance(info, str)

    def test_check_level(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        dev.set_level(0)
        self.assertIsInstance(dev.check_level(), int)

    def test_set_level(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.set_level(0), int)


if __name__=='__main__':
    unittest.main()