#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
"""

import communicator

class ni_usb(communicator.communicator):
    """
    """
    devname = 'Dev1'

    def __init__(self, devname):
        """
        """
        self.devname = devname
        pass

