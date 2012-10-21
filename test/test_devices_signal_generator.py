#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""


TARGET = ('192.168.100.211', 7777)
COMMAND_TYPE = 'SCPI'
CONNECTION_METHOD = 'Ethernet'


import pymeasure
import pymeasure.devices
import pymeasure.communicators

import unittest


class Test_Signal_Generator(unittest.TestCase):
    def test_initialize(self):
        self.assertIsInstance(pymeasure.devices.signal_generator(COMMAND_TYPE),
                              pymeasure.devices.dev_signal_generator.signal_generator)

    def test_set_communicator(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE)
        self.assertIsInstance(sg.set_communicator(com),
                              pymeasure.communicators.communicator.communicator)

    def test_get_product_information(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE)
        self.assertIsNotNone(sg.set_communicator(com))
        info = sg.get_product_information()
        self.assertIsInstance(info, str)

    def test_check_freq(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE, com)
        self.assertIsInstance(sg.check_freq(), float)

    def test_set_freq(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE, com)
        self.assertEqual(sg.set_freq(1.2345678e9, 'Hz'), 1.2345678e9)
        self.assertEqual(sg.set_freq(1.2345678e5, 'Hz'), 1.2345678e5)
        self.assertEqual(sg.set_freq(1.2345678e6, 'kHz'), 1.2345678e9)
        self.assertEqual(sg.set_freq(1.2345678e2, 'kHz'), 1.2345678e5)
        self.assertEqual(sg.set_freq(1.2345678e1, 'MHz'), 1.2345678e7)
        self.assertEqual(sg.set_freq(1.23456e-1, 'MHz'), 1.23456e5)
        self.assertEqual(sg.set_freq(1.234567, 'GHz'), 1.234567e9)
        self.assertEqual(sg.set_freq(1.e-4, 'GHz'), 1.e5)

    def test_check_power(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE, com)
        self.assertIsInstance(sg.check_power(), float)

    def test_set_power(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE, com)
        self.assertEqual(sg.set_power(-10, 'dBm'), -10)
        self.assertEqual(sg.set_power(-15, 'dBm'), -15)
        self.assertEqual(sg.set_power(-20, 'dBm'), -20)

    def test_check_output(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE, com)
        self.assertIsInstance(sg.check_output(), int)

    def test_output_on_off(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        sg = pymeasure.devices.signal_generator(COMMAND_TYPE, com)
        self.assertEqual(sg.output_on(), 1)
        self.assertEqual(sg.output_off(), 0)




if __name__=='__main__':
    unittest.main()