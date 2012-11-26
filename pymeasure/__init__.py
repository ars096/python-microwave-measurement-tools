#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import communicators
import devices

def create_communicator(communication_method, *args, **kwargs):
    method = communication_method.lower()

    if method in ['ethernet', 'lan']:
        return communicators.ethernet(*args, **kwargs)

    elif method in ['gpib_prologix', 'gpib-prologix', 'prologix']:
        return communicators.gpib_prologix(*args, **kwargs)

    elif method in ['ni_usb']:
        return communicators.ni_usb(*args, **kwargs)

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

def coaxial_switch(command_type, communication_method, *args, **kwargs):
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.coaxial_switch(command_type, com)

def attenuator(command_type, communication_method, *args, **kwargs):
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.attenuator(command_type, com)
