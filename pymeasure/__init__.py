#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import communicators
import devices

def create_communicator(communication_method, *args, **kwargs):
    if communication_method.lower()=='ethernet': return create_ethernet(*args, **kwargs)
    if communication_method.lower()=='gpib_prologix': return create_gpib_prologix(*args, **kwargs)
    return None

def create_ethernet(host, port):
    return communicators.ethernet(host, port)

def create_gpib_prologix(host, port, gpibport):
    return communicators.gpib_prologix(host, port, gpibport)


def create_signalgenerator(command_type, communication_method, *args, **kwargs):
    """
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.signal_generator(command_type, com)



class creator(object):
    """
    """
    pass



