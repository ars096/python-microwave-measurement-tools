#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import communicators
import devices

def create_communicator(communication_method, *args, **kwargs):
    mehtod = communication_method.lower()
    if method=='ethernet': return communicators.ethernet(*args, **kwargs)
    elif method=='gpib_prologix': return communicators.gpib_prologix(*args, **kwargs)
    elif method=='ni_usb': return communicators.ni_usb(*args, **kwargs)
    return None

def signalgenerator(command_type, communication_method, *args, **kwargs):
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.signal_generator(command_type, com)

def powermeter(command_type, communication_method, *args, **kwargs):
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.power_meter(command_type, com)

def spectrumanalyzer(command_type, communication_method, *args, **kwargs):
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.spectrum_analyzer(command_type, com)

def io(command_type, communication_method, *args, **kwargs):
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.io(command_type, com)


