#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""


TARGET = ('192.168.100.182', 5025)
COMMAND_TYPE = 'SCPI'
CONNECTION_METHOD = 'Ethernet'


import pymeasure
import pymeasure.devices
import pymeasure.communicators

import unittest

create_test_device = pymeasure.devices.spectrum_analyzer
device_under_the_test = pymeasure.devices.dev_spectrum_analyzer.spectrum_analyzer

freq_variation = [(1, 'GHz', 1e9),
                  (5, 'GHz', 5e9),
                  (10, 'GHz', 10e9),
                  (1000, 'MHz', 1e9),]

class Test_Spectrum_Analyzer(unittest.TestCase):
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

    def test_check_freq_center(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_freq_center(), float)

    def test_set_freq_center(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        [self.assertEqual(dev.set_freq_center(v[0], v[1]), v[2]) for v in freq_variation]

    def test_check_freq_start(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_freq_start(), float)

    def test_set_freq_start(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        [self.assertEqual(dev.set_freq_start(v[0], v[1]), v[2]) for v in freq_variation]

    def test_check_freq_stop(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_freq_stop(), float)

    def test_set_freq_stop(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        [self.assertEqual(dev.set_freq_stop(v[0], v[1]), v[2]) for v in freq_variation]

    def test_check_freq_span(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_freq_span(), float)

    def test_set_average(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertEqual(dev.set_average(0), 0)
        self.assertEqual(dev.set_average(10), 10)
        self.assertEqual(dev.set_average(50), 50)
        self.assertEqual(dev.set_average(0), 0)

    def test_check_average(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_average(), float)

    def test_set_resolution_bandwidth(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertEqual(dev.set_resolution_bandwidth('auto'), -1)
        self.assertEqual(dev.set_resolution_bandwidth(1, 'MHz'), 1e6)
        self.assertEqual(dev.set_resolution_bandwidth(10, 'kHz'), 10e3)
        self.assertEqual(dev.set_resolution_bandwidth(3, 'MHz'), 3e6)

    def test_check_resolution_bandwidth(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_resolution_bandwidth(), float)

    def test_set_sweep_points(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertEqual(dev.set_sweep_points(101), 101)
        self.assertEqual(dev.set_sweep_points(501), 501)
        self.assertEqual(dev.set_sweep_points(1001), 1001)
        self.assertEqual(dev.set_sweep_points(4001), 4001)
        self.assertEqual(dev.set_sweep_points(601), 601)

    def test_check_sweep_points(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        self.assertIsInstance(dev.check_sweep_points(), float)

    def test_measure(self):
        com = pymeasure.create_communicator(CONNECTION_METHOD, *TARGET)
        dev = create_test_device(COMMAND_TYPE, com)
        points = dev.check_sweep_points()
        spec = dev.measure()
        self.assertIsInstance(spec[0], float)
        self.assertEqual(len(spec), points)



if __name__=='__main__':
    unittest.main()