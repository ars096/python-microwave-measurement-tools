#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""


TARGET = ('192.168.100.220', 1234, 13)
COMMAND_TYPE = 'Anritsu'
CONNECTION_METHOD = 'GPIB_PROLOGIX'

import pymeasure
import pymeasure.devices
import pymeasure.communicators

import unittest


class Test_Power_Meter(unittest.TestCase):
    def test_initialize(self):
        self.assertIsInstance(pymeasure.devices.power_meter(COMMAND_TYPE),
                              pymeasure.devices.dev_power_meter.power_meter)

    def test_set_communicator(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        pm = pymeasure.devices.power_meter(COMMAND_TYPE)
        self.assertIsInstance(pm.set_communicator(com),
                              pymeasure.communicators.communicator.communicator)

    def test_measure(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        pm = pymeasure.devices.power_meter(COMMAND_TYPE, com)
        self.assertIsInstance(pm.measure(), float)

    def test_check_average(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        pm = pymeasure.devices.power_meter(COMMAND_TYPE, com)
        self.assertIsInstance(pm.check_average(), int)

#    def test_set_average(self):
#        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
#        pm = pymeasure.devices.power_meter(COMMAND_TYPE, com)
#        self.assertEqual(pm.set_average(10), 10)
#        self.assertEqual(pm.set_average(20), 20)
#        self.assertEqual(pm.set_average(30), 30)

    def test_check_unit(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        pm = pymeasure.devices.power_meter(COMMAND_TYPE, com)
        self.assertEqual(pm.check_unit(), 'DBM')


    def test_set_unit(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        pm = pymeasure.devices.power_meter(COMMAND_TYPE, com)
        self.assertEqual(pm.set_unit('DBM'), 'DBM')


if __name__=='__main__':
    unittest.main()