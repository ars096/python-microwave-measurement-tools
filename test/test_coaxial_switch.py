#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""


TARGET = ('192.168.100.220', 1234, 28)
COMMAND_TYPE = 'SCPI'
CONNECTION_METHOD = 'GPIB_PROLOGIX'

import pymeasure
import pymeasure.devices
import pymeasure.communicators
import unittest

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



if __name__=='__main__':
    unittest.main()