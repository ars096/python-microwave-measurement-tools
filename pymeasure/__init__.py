#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import communicators
import devices

def create_communicator(communication_method, *args, **kwargs):
    if communication_method.lower()=='ethernet': return create_ethernet(*args, **kwargs)
    return None

def create_ethernet(host, port):
    com = communicators.ethernet(host, port)
    return com


def create_powermeter(command_type, communication_method, *args, **kwargs):
    """
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.signal_generator(command_type, com)



class creator(object):
    """
    """
    pass



