#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import time
import device

set_sleep = 0.5

def select_spectrum_analyzer(command_type, *args, **kwargs):
    command_type = command_type.lower()
    if command_type=='scpi': return SCPI_command(*args, **kwargs)
    #if command_type=='anritsu': return anritsu_command(*args, **kwargs)
    #if command_type=='phasematrix': return phasematrix_command(*args, **kwargs)
    return None

class spectrum_analyzer(object):
    @device._open_close
    def set_freq_center(self, freq):
        pass

    @device._open_close
    def check_freq_center(self):
        pass

    @device._open_close
    def set_freq_start(self, freq):
        pass

    @device._open_close
    def check_freq_start(self):
        pass

    @device._open_close
    def set_freq_stop(self, freq):
        pass

    @device._open_close
    def check_freq_stop(self):
        pass

    @device._open_close
    def set_freq_span(self, bandwidth):
        pass

    @device._open_close
    def check_freq_span(self):
        pass

    @device._open_close
    def set_average(self, average_num):
        pass

    @device._open_close
    def check_time_average(self):
        pass

    @device._open_close
    def set_resolution_bandwidth(self, bandwidth, unit='MHz'):
        pass

    @device._open_close
    def check_resolution_bandwidth(self):
        pass

    @device._open_close
    def set_unit(self, unit):
        pass

    @device._open_close
    def check_unit(self):
        pass

    @device._open_close
    def set_yrange(self, yrange):
        pass

    @device._open_close
    def check_yrange(self):
        pass

    @device._open_close
    def measure(self):
        pass


class SCPI_command(spectrum_analyzer, device.scpi_device):
    """
    tested products
    ===============
        Agilent Technologies
        --------------------
            E4440A, socket port = 5025

    """
    @device._open_close
    def set_freq_center(self, freq, unit='MHz'):
        self.com.send(':FREQ:CENTER %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_center()

    @device._open_close
    def check_freq_center(self):
        self.com.send(':FREQ:CENTER?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_start(self, freq, unit='MHz'):
        self.com.send(':FREQ:START %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_start()

    @device._open_close
    def check_freq_start(self):
        self.com.send(':FREQ:START?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_stop(self, freq, unit='MHz'):
        self.com.send(':FREQ:STOP %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_stop()

    @device._open_close
    def check_freq_stop(self):
        self.com.send(':FREQ:STOP?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_span(self, freq, unit='MHz'):
        self.com.send(':FREQ:SPAN %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_span()

    @device._open_close
    def check_freq_span(self):
        self.com.send(':FREQ:SPAN?')
        return float(self.com.readline())

    @device._open_close
    def check_average(self):
        self.com.send(':AVERAGE?')
        average_onoff = float(self.com.readline())
        if average_onoff==0.: return 0.
        self.com.send(':AVERAGE:COUNT?')
        return float(self.com.readline())

    @device._open_close
    def set_average(self, average_num):
        if average_num==0:
            self.com.send(':AVERAGE OFF')
        else:
            self.com.send(':AVERAGE ON')
            self.com.send(':AVERAGE:COUNT %d'%average_num)
        time.sleep(set_sleep)
        return float(self.check_average())

    @device._open_close
    def check_resolution_bandwidth(self):
        self.com.send(':BANDWIDTH:RESOLUTION:AUTO?')
        auto = float(self.com.readline())
        if auto==1.: return -1.
        self.com.send(':BANDWIDTH:RESOLUTION?')
        return float(self.com.readline())

    @device._open_close
    def set_resolution_bandwidth(self, bandwidth, unit='MHz'):
        if bandwidth=='auto':
            self.com.send(':BANDWIDTH:RESOLUTION:AUTO ON')
            return float(self.check_resolution_bandwidth())
        self.com.send(':BANDWIDTH:RESOLUTION %f %s'%(bandwidth, unit))
        return float(self.check_resolution_bandwidth())

