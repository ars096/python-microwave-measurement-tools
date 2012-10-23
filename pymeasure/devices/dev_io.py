#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_io(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return SCPI_command(*args, **kwargs)
    return None


class io(object):
    @device._open_close
    def set_analog_output(self, level, ch):
        pass

    @device._open_close
    def check_analog_output(self, ch):
        pass

    @device._open_close
    def check_analog_input(self, ch):
        pass

    @device._open_close
    def set_digital_output(self, ch):
        pass

    @device._open_close
    def check_digital_output(self, ch):
        pass

    @device._open_close
    def check_digital_input(self, ch):
        pass

