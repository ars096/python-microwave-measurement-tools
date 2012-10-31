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
    def set_close_switch(self, ch):
      pass

    @device._open_close
    def check_close_switch(self, ch):
        pass

    @device._open_close
    def set_all_close_switch(self):
        pass


class SCPI_command(coaxial_switch, device.scpi_device):
    @device._open_close
    def check_supply_voltage(self, ch=1):
        """
        -- Method --
        query supply voltage to coaxial switch
        """
        self.com.send('CONFigure:BANK%d?' %ch)
        return int(self.com.readline().strip("\n")[1:])

    @device._open_close
    def set_supply_voltage(self, ch=1):
        """
        -- Method --
        set supply voltage to coaxial switch
        note that "Agilent 11713B" sets only supply DC 24V
        """
        self.com.send('CONFigure:BANK%d P24v'%ch)
        return self.check_supply_voltage(ch)

    @device._open_close
    def check_open_switch(self, ch='201:208'):
        """
        -- Method --
        query open switching path.
        """
        self.com.send(':ROUTe:OPEn? (@%s)'%ch)
        return map(int, self.com.readline().strip('\n').split(','))

    @device._open_close
    def check_close_switch(self, ch='201:208'):
        """
        -- Method --
        query close switching path
        """
        self.com.send(':ROUTe:CLOSe? (@%s)'%ch)
        return map(int, self.com.readline().strip('\n').split(','))

    @device._open_close
    def set_open_switch(self, ch='101:104'):
        """
        -- Method --
        set open switching path
        """
        self.com.send(':ROUTe:OPEn (@%s)'%ch)
        return self.check_open_switch(ch)

    @device._open_close
    def set_close_switch(self, ch='101:104'):
        """
        -- Method --
        set close switching path
        """
        self.com.send(':ROUTe:CLOSe (@%s)'%ch)
        return self.check_close_switch(ch)


    def set_all_close_switch(self):
        """
        -- Method --
        set close switching path
        """
        self.com.send(':ROUTe:CLOSe:ALL')
        return self.check_close_switch(ch='101:108')