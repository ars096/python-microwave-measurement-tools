#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_power_meter(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return SCPI_command(*args, **kwargs)
    if command_type=='anritsu': return anritsu_command(*args, **kwargs)
    return None


class power_meter(object):
    def measure(self, ch=1):
        pass

    def set_average(self, average, ch=1):
        pass

    def check_average(self, ch=1):
        pass

    def set_unit(self, units, ch=1):
        pass

    def check_unit(self, ch=1):
        pass




class anritsu_command(power_meter, device.device):
    @device._open_close
    def measure(self, ch=1):
        """
        -- Method --
        retrieve a value of power meter
        """
        self.com.send('O %d' %ch)
        return float(self.com.readline())

    #@device._open_close
    def set_average(self, average, ch=1):
        """
        -- Method --
        set average by time
        mode is always 'AUTO'
        """
        #TODO:someday
        if ch == 1: ch = 'A'
        elif ch == 2: ch = 'B'
        self.com.open()
        self.com.send('AVG %s, AUTO, %d'%(ch, average))
        self.com.close()
        import time
        time.sleep(1)
        return self.check_average(ch)

    @device._open_close
    def check_average(self, ch=1):
        """
        -- Method --
        check average by time
        """
        if ch == 1: ch = 'A'
        elif ch == 2: ch = 'B'
        self.com.send('AVG? %s'%ch)
        a = int(self.com.readline().split(',')[-1])
        return a



    @device._open_close
    def check_unit(self, ch=1):
        """
        -- Method --
        check units
        """
        self.com.send('CHUNIT? %d' %ch)
        return self.com.readline().strip().split(',')[-1]

    @device._open_close
    def set_unit(self, units, ch=1):
        """
        -- Method --
        set unit ([dBm] or [W] or [DBUV) or [DBMW]
        """
        self.com.send('CHUNIT %d, %s' %(ch,units))
        return self.check_unit(ch)
