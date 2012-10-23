#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_spectrum_analyzer(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return SCPI_command(*args, **kwargs)
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
    def set_freq_range(self, bandwidth):
        pass

    @device._open_close
    def check_freq_range(self):
        pass

    @device._open_close
    def set_time_average(self, average_sec):
        pass

    @device._open_close
    def check_time_average(self):
        pass

    @device._open_close
    def set_resolution_bandwidth(self, bandwidth):
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



