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

class Test_attenuator(unittest.TestCase):
    def test_initialize(self):
        self.assertIsInstance(pymeasure.devices.attenuator(COMMAND_TYPE),
                              pymeasure.devices.dev_attenuator.attenuator)

    def test_set_communicator(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        att = pymeasure.devices.attenuator(COMMAND_TYPE, com)
        self.assertIsInstance(att.set_communicator(com),
                              pymeasure.communicators.communicator.communicator)

    def test_set_level(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        att = pymeasure.devices.attenuator(COMMAND_TYPE, com)
        att.set_level()
