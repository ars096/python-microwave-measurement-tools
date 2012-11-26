#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import numpy
import device

def select_io(command_type, *args, **kwargs):
    command_type = command_type.lower()
    if command_type=='ni_daq': return ni_daq(*args, **kwargs)
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


class ni_daq(io, device.device):
    devname = 'Dev1'
    ai_range = [-10., 10.]
    ai_terminal = 'default'
    terminal_list = ['default', 'rse', 'nrse', 'diff', 'pseudodiff']

    def __init__(self, communicator=None):
        if not communicator is None: self.devname = communicator.devname
        device.device.__init__(self, communicator)
        pass

    def set_device(self, devname):
        self.devname = devname
        return self.devname

    def set_ai_range(self, min_val=None, max_val=None):
        if min_val is not None: self.ai_range[0] = min_val
        if max_val is not None: self.ai_range[1] = max_val
        return self.ai_range

    def set_ai_terminal(self, terminal_type):
        if not terminal_type.lower() in self.terminal_list:
            print('bad argument: %s'%terminal_type)
            print('terminal type should be %s'%(self.terminal_list))
        else:
            self.ai_terminal = terminal_type.lower()
        return self.ai_terminal

    @device._open_close
    def set_analog_output(self, level, ch):
        pass

    @device._open_close
    def check_analog_output(self, ch):
        pass

    @device._open_close
    def check_analog_input(self, ch):
        import nidaqmx
        task = nidaqmx.AnalogInputTask()
        task.create_voltage_channel('%s/ai%d',
                                    terminal=self.ai_terminal,
                                    min_val=self.ai_range[0],
                                    max_val=self.ai_range[1])
        task.start()
        d = task.read(100)
        return numpy.average(d)

    @device._open_close
    def set_digital_output(self, ch):
        pass

    @device._open_close
    def check_digital_output(self, ch):
        pass

    @device._open_close
    def check_digital_input(self, ch):
        pass

