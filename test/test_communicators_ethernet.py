#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

TARGET = ('google.com', 80)
DUMMY = ('google.comcom', 80)


import pymeasure.communicators

import unittest

class Test_Network_via_www(unittest.TestCase):
    def test_initialize(self):
        self.assertIsInstance(pymeasure.communicators.ethernet(*TARGET),
                              pymeasure.communicators.communicator.communicator)

    def test_open_close(self):
        import socket
        # valid case
        com = pymeasure.communicators.ethernet(*TARGET)
        self.assertIsInstance(com.open(), socket.socket)
        self.assertIsNone(com.close())

        # in valid case
        com = pymeasure.communicators.ethernet(*DUMMY, timeout=1)
        self.assertIsNone(com.open())

    def test_set_timeout(self):
        com = pymeasure.communicators.ethernet(*DUMMY)
        self.assertEqual(com.set_timeout(1), 1)
        self.assertIsNone(com.open())

    def test_send(self):
        com = pymeasure.communicators.ethernet(*TARGET)
        self.assertIsNotNone(com.open())
        self.assertIsInstance(com.send('GET / HTTP/1.1\n\n'), int)
        self.assertIsNone(com.close())

    def test_recv(self):
        com = pymeasure.communicators.ethernet(*TARGET)

        # normal case
        self.assertIsNotNone(com.open())
        self.assertIsInstance(com.send('GET / HTTP/1.1\n\n'), int)
        self.assertIsInstance(com.recv(1000), str)
        # using term_char option
        self.assertIsInstance(com.send('GET / HTTP/1.1', term_char='\n\n'), int)
        self.assertIsInstance(com.recv(1000), str)

        self.assertIsNone(com.close())

    def test_set_default_term_char(self):
        com = pymeasure.communicators.ethernet(*TARGET)
        self.assertIsNotNone(com.open())
        com.set_default_sending_term_char('\n\n')
        self.assertIsInstance(com.send('GET / HTTP/1.1'), int)
        self.assertIsInstance(com.recv(1000), str)
        self.assertIsNone(com.close())

    def test_set_default_recv_byte(self):
        com = pymeasure.communicators.ethernet(*TARGET)
        self.assertIsNotNone(com.open())
        self.assertIsInstance(com.send('GET / HTTP/1.1\n\n'), int)
        self.assertEqual(len(com.recv()),
                         pymeasure.communicators.com_ethernet.ethernet.default_recv_byte)
        com.set_default_recv_byte(150)
        self.assertEqual(len(com.recv(150)), 150)
        self.assertIsNone(com.close())

    def test_readline(self):
        com = pymeasure.communicators.ethernet(*TARGET)
        self.assertIsNotNone(com.open())
        com.set_default_recv_byte(5)
        self.assertIsInstance(com.send('GET / HTTP/1.1\n\n'), int)
        ret = com.readline('\r\n')
        self.assertEqual(len(ret.split('\r\n')), 2)
        self.assertIsNone(com.close())


if __name__=='__main__':
    unittest.main()