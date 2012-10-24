#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_coaxial_switch(command_type, *args, **kwargs):
    command_type = command_type.lower()
    if command_type=='scpi': return SCPI_command(*args, **kwargs)
    return None


class coaxial_switch(object):
    @device._open_close
    def check_supply_voltage(self):
        pass

    @device._open_close
    def set_supply_voltage(self):
        pass

    @device._open_close
    def set_open_switch(self, ch):
        pass

    @device._open_close
    def check_open_switch(self, ch):
        pass

    @device._open_close
    def set_close_swicth(self, ch):
        pass

    @device._open_close
    def check_close_switch(self, ch):
        pass


class SCPI_command(coaxial_switch, device.scpi_device):
    @device._open_close
    def check_supply_voltage(self, ch=1):
        """
        -- Method --
        query supply voltage
        """
        self.com.send('CONFigure:BANK%d?' %ch)
        return self.com.readline()


#    @device._open_close
#    def set_supply_voltage(self):
#        self.com.send('CONFigure:BANK%d P24v')
#        return self.check_supply_voltage(ch)

    @device._open_close
    def set_open_switch(self, ch):
        pass

    @device._open_close
    def check_open_switch(self, ch):
        pass

    @device._open_close
    def set_close_swicth(self, ch):
        pass

    @device._open_close
    def check_close_switch(self, ch):
        pass
