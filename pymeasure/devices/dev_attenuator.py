#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_attenuator(command_type, *args, **kwargs):
    command_type = command_type.lower()
    if command_type=='scpi': return SCPI_command(*args, **kwargs)
    if command_type=='elva1': return ELVA1_command(*args, **kwargs)
    return None


class attenuator(object):
    @device._open_close
    def set_level(self, level):
        pass

class ELVA1_command(attenuator, device.device):
    @device._open_close
    def set_level(self, level=0):
        self.com.send('PO %X'%level)
