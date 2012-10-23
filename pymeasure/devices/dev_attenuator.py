#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_attenuator(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return SCPI_command(*args, **kwargs)
    return None


class attenuator(object):
    @device._open_close
    def set_level(self, level, ch=1):
        pass

    @device._open_close
    def check_level(self, ch=1):
        pass

