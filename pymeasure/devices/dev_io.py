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
    #if command_type=='scpi': return scpi_command(*args, **kwargs)
    return None


class io(object):
    def set_analog_output(self, level, ch):
        pass

    def check_analog_output(self, ch):
        pass

    def check_analog_input(self, ch):
        pass

    def set_digital_output(self, ch):
        pass

    def check_digital_output(self, ch):
        pass

    def check_digital_input(self, ch):
        pass


class ni_daq(io, device.device):
    devname = 'Dev1'
    ai_range = [-10., 10.]
    ai_terminal = 'default'
    ao_range = [-10., 10.]
    ao_data = {}
    terminal_list = ['default', 'rse', 'nrse', 'diff', 'pseudodiff']

    def __init__(self, communicator=None):
        if communicator is not None: self.devname = communicator.devname
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

    def set_ao_range(self, min_val=None, max_val=None):
        if min_val is not None: self.ao_range[0] = min_val
        if max_val is not None: self.ao_range[1] = max_val
        return self.ao_range

    def set_analog_output(self, level, ch=0):
        import nidaqmx
        task = nidaqmx.AnalogOutputTask()
        task.create_voltage_channel('%s/ao%d'%(self.devname, ch),
                                    min_val=self.ao_range[0],
                                    max_val=self.ao_range[1])
        task.write([level]*2)
        del(task)
        self.ao_data[ch] = level
        return self.check_analog_output(ch)

    def sweep_analog_output(self, min, max, cycle=1, ch=0):
        data = numpy.concatenate([numpy.linspace(min, max, 501),
                                  numpy.linspace(max, min, 501)])
        self._sweep_analog_output(data, cycle, ch)
        return

    def _sweep_analog_output(self, data, cycle=1, ch=0):
        import nidaqmx
        num = len(data)

        task = nidaqmx.AnalogOutputTask()
        task.create_voltage_channel('%s/ao%d'%(self.devname, ch),
                                    min_val=self.ao_range[0],
                                    max_val=self.ao_range[1])
        task.configure_timing_sample_clock(rate=num*cycle)
        task.write(data)
        #task.start()
        raw_input('Enter any key to stop sweeping')
        task.stop()
        del(task)
        return

    def check_analog_output(self, ch=0):
        return self.ao_data.get(ch, None)

    def check_analog_input(self, ch=0):
        import nidaqmx
        task = nidaqmx.AnalogInputTask()
        task.create_voltage_channel('%s/ai%d'%(self.devname, ch),
                                    terminal=self.ai_terminal,
                                    min_val=self.ai_range[0],
                                    max_val=self.ai_range[1])
        task.start()
        d = task.read(100)
        del(task)
        return numpy.average(d)

    def set_digital_output(self, ch):
        pass

    def check_digital_output(self, ch):
        pass

    def check_digital_input(self, ch):
        pass

