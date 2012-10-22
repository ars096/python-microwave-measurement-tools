#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import socket

import communicator

class ethernet(communicator.communicator):
    """
    """
    type = 'Ethernet'
    timeout = None  # in seconds
    host = None
    port = None
    s = None # socket

    def __init__(self, host, port, timeout=None):
        """
        """
        self.host = host
        self.port = port
        self.timeout = timeout
        pass

    def _get_communication_instance(self):
        return self.s

    def _open(self):
        """
        """
        try:
            s = socket.socket()
            s.settimeout(self.timeout)
            s.connect((self.host, self.port))
        except socket.error, e:
            print('socket.error::%s in %s.open'%(e, type(self)))
            #raise socket.error, e
            s = None
            pass
        self.s = s
        return self._get_communication_instance()

    def _close(self):
        """
        """
        self.s.close()
        self.s = None
        return self.s

    def set_timeout(self, sec):
        """
        """
        self.timeout = sec
        if self.s is not None:
            self.s.settimeout(sec)
            pass
        return self.timeout

    def _recv(self, byte):
        """
        """
        return self.s.recv(byte)

    def _send(self, msg):
        """
        """
        return self.s.send(msg)

