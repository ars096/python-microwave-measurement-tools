#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
"""

import com_ethernet

class gpib_prologix(com_ethernet.ethernet):
    """
    """
    type = 'GPIB'
    timeout = None # in second
    host = None
    port = None
    gpibport = None
    s = None

    def __init__(self, host, port, gpibport, timeout=None):
        """
        """
        self.host = host
        self.port = port
        self.gpibport = gpibport
        self.timeout = timeout
        pass

    def set_mode_device(self):
        return self.s.send('++mode 0')

    def set_mode_controller(self):
        return self.s.send('++mode 1')

    def set_auto_listen(self):
        return self.s.send('++auto 0')

    def set_auto_talk(self):
        return self.s.send('++auto 1')

    def set_gpibport(self):
        return self.s.send('++addr %d'%(self.gpibport))

    def _close(self):
        """
        """
        self.set_mode_device()
        self.s.close()
        self.s = None
        return self.s

    def _recv(self, byte):
        """
        """
        self.set_auto_talk()
        return self.s.recv(byte)

    def _send(self, msg):
        """
        """
        self.set_mode_controller()
        self.set_gpibport()
        self.set_auto_listen()
        return self.s.send(msg)


