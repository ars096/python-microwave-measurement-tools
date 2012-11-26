#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

#TARGET = ('192.168.100.220', 1234, 28)
#COMMAND_TYPE = 'Agilent11713B'
#CONNECTION_METHOD = 'GPIB-Prologix'

TARGET = ('192.168.100.183', 5025)
COMMAND_TYPE = 'Agilent11713C'
CONNECTION_METHOD = 'Ethernet'

import pymeasure
import pymeasure.devices
import pymeasure.communicators
import unittest


create_test_device = pymeasure.devices.coaxial_switch
device_under_the_test = pymeasure.devices.dev_coaxial_switch.coaxial_switch

class Test_Coaxial_Switch(unittest.TestCase):
    def test_initialize(self):
        self.assertIsInstance(create_test_device(COMMAND_TYPE),
                              device_under_the_test)

    def test_set_communicator(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE)
        self.assertIsInstance(dev.set_communicator(com),
                              pymeasure.communicators.communicator.communicator)

    def test_get_product_information(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE)
        self.assertIsNotNone(dev.set_communicator(com))
        info = dev.get_product_information()
        print(info)
        self.assertIsInstance(info, str)

    def test_check_ch(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_ch(), tuple)

    def test_set_ch(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.set_ch(1), tuple)
        self.assertIsNone(dev.set_ch(0))
        self.assertIsNone(dev.set_ch(-1))
        self.assertEqual(dev.set_ch(2)[0], 2)
        self.assertEqual(dev.set_ch(1)[0], 1)


"""
class Test_Coaxial_Switch(unittest.TestCase):
    def test_initialize(self):
        self.assertIsInstance(pymeasure.devices.coaxial_switch(COMMAND_TYPE),
                              pymeasure.devices.dev_coaxial_switch.coaxial_switch)

    def test_set_communicator(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        cs = pymeasure.devices.coaxial_switch(COMMAND_TYPE)
        self.assertIsInstance(cs.set_communicator(com),
                              pymeasure.communicators.communicator.communicator)

    def test_check_supply_voltage(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        cs = pymeasure.devices.coaxial_switch(COMMAND_TYPE, com)
        self.assertIsInstance(cs.check_supply_voltage(), int)

    def test_set_supply_voltage(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        cs = pymeasure.devices.coaxial_switch(COMMAND_TYPE, com)
        cs.set_supply_voltage()
        self.assertIsInstance(cs.check_supply_voltage(), int)

    def test_check_open_switch(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        cs = pymeasure.devices.coaxial_switch(COMMAND_TYPE, com)
        self.assertIsInstance(cs.check_open_switch(), list)

    def test_check_close_switch(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        cs = pymeasure.devices.coaxial_switch(COMMAND_TYPE, com)
        self.assertIsInstance(cs.check_close_switch(), list)


    def test_set_open_switch(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        cs = pymeasure.devices.coaxial_switch(COMMAND_TYPE, com)
        self.assertIsInstance(cs.set_open_switch(), list)


    def test_set_close_switch(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        cs = pymeasure.devices.coaxial_switch(COMMAND_TYPE, com)
        self.assertIsInstance(cs.set_close_switch(), list)
"""



if __name__=='__main__':
    unittest.main()