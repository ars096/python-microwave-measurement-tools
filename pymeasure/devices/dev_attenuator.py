#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_attenuator(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return SCPI_command(*args, **kwargs)
    if command_type in ['elva1', 'elva-1']:
        return elva1_command(*args, **kwargs)
    return None


class attenuator(object):
    def set_level(self, level):
        pass

    def check_level(self, level):
        pass


class elva1_command(attenuator, device.scpi_device):
    """
    tested products
    ===============
        ELVA1
        -----------
            GPDVC-15/100/RS, GPIB

    """
    level = None

    def check_level(self):
        return self.level

    @device._open_close
    def set_level(self, level=0):
        self.com.send('PO %04X'%int(level))
        self.level = int(level)
        return self.check_level()

    @device._open_close
    def get_gpib_address(self):
        self.com.send('SYST:COMM:GPIB:ADDR?')
        return int(self.com.readline())

    @device._open_close
    def set_gpib_address(self, gpib):
        self.com.send('SYST:COMM:GPIB:ADDR %d'%gpib)
        self.com.set_gpib_address(gpib)
        self.com.send('*SAV 0')
        return self.get_gpib_address()

