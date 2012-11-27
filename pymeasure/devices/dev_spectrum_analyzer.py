#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import time
import numpy
import device

set_sleep = 0.3

def select_spectrum_analyzer(command_type, *args, **kwargs):
    command_type = command_type.lower()
    if command_type=='scpi': return scpi(*args, **kwargs)
    if command_type=='hp8590': return hp8590(*args, **kwargs)
    #if command_type=='anritsu': return anritsu_command(*args, **kwargs)
    #if command_type=='phasematrix': return phasematrix_command(*args, **kwargs)
    return None

class spectrum_analyzer(object):
    def get_axis(self):
        start = self.check_freq_start()
        end = self.check_freq_stop()
        num = self.check_sweep_points()
        return numpy.linspace(start, end, num)

    def set_freq_center(self, freq):
        pass

    def check_freq_center(self):
        pass

    def set_freq_start(self, freq):
        pass

    def check_freq_start(self):
        pass

    def set_freq_stop(self, freq):
        pass

    def check_freq_stop(self):
        pass

    def set_freq_span(self, bandwidth):
        pass

    def check_freq_span(self):
        pass

    def set_average(self, average_num):
        pass

    def check_average(self):
        pass

    def set_resolution_bandwidth(self, bandwidth, unit='MHz'):
        pass

    def check_resolution_bandwidth(self):
        pass

    def set_sweep_points(self, points):
        pass

    def check_sweep_points(self):
        pass

    def set_unit(self, unit):
        pass

    def check_unit(self):
        pass

    def set_yrange(self, yrange):
        pass

    def check_yrange(self):
        pass

    def measure(self):
        pass


class scpi(spectrum_analyzer, device.scpi_device):
    """
    tested products
    ===============
        Agilent Technologies
        --------------------
            E4440A, Ethernet(port=5025)
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

    @device._open_close
    def set_sweep_points(self, points):
        self.com.send(':SENSE:SWEEP:POINTS %d'%(points))
        return self.check_sweep_points()

    @device._open_close
    def check_sweep_points(self):
        self.com.send(':SENSE:SWEEP:POINTS?')
        return int(self.com.readline())

    @device._open_close
    def measure(self):
        self.com.send(':TRACE:DATA? TRACE1')
        spectrum_str = self.com.readline()
        spectrum = numpy.array(spectrum_str.split(','), dtype=float)
        return spectrum

class hp8590(spectrum_analyzer, device.device):
    """
    tested products
    ===============
        Agilent Technologies
        --------------------
            8596E, GPIB
    """
    @device._open_close
    def get_product_information(self):
        self.com.send('ID?')
        id = self.com.readline()
        self.com.send('SER?')
        ser = self.com.readline()
        self.com.send('REV?')
        rev = self.com.readline()
        idn =  'Agilent Technologies, %s, %s, %s'%(id.strip(),
                                                   ser.strip(),
                                                   rev)
        self.product_information = idn
        return self.product_information

    @device._open_close
    def set_freq_center(self, freq, unit='MHz'):
        self.com.send('CF %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_center()

    @device._open_close
    def check_freq_center(self):
        self.com.send('CF?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_start(self, freq, unit='MHz'):
        self.com.send('FA %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_start()

    @device._open_close
    def check_freq_start(self):
        self.com.send('FA?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_stop(self, freq, unit='MHz'):
        self.com.send('FB %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_stop()

    @device._open_close
    def check_freq_stop(self):
        self.com.send('FB?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_span(self, freq, unit='MHz'):
        self.com.send('SP %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_span()

    @device._open_close
    def check_freq_span(self):
        self.com.send('SP?')
        return float(self.com.readline())

    @device._open_close
    def check_average(self):
        self.com.send('VAVG?')
        return float(self.com.readline())

    @device._open_close
    def set_average(self, average_num):
        if average_num==0:
            self.com.send('VAVG OFF')
        else:
            self.com.send('VAVG ON')
            self.com.send('VAVG %d'%average_num)
        time.sleep(set_sleep)
        return float(self.check_average())

    @device._open_close
    def check_resolution_bandwidth(self):
        self.com.send('RB?')
        return float(self.com.readline())

    @device._open_close
    def set_resolution_bandwidth(self, bandwidth, unit='MHz'):
        if bandwidth=='auto':
            self.com.send('RB AUTO')
            return float(self.check_resolution_bandwidth())
        self.com.send('RB %f %s'%(bandwidth, unit))
        return float(self.check_resolution_bandwidth())

    @device._open_close
    def set_sweep_points(self, points):
        return self.check_sweep_points

    @device._open_close
    def check_sweep_points(self):
        return 401

    @device._open_close
    def measure(self):
        self.com.send('TRA?')
        spectrum_str = self.com.readline()
        spectrum = numpy.array(spectrum_str.split(','), dtype=float)
        return spectrum

