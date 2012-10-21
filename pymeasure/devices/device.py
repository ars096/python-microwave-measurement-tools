#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

def _open_close(func):
    def _do(cls, *args, **kwargs):
        assert cls.com is not None, 'communicator is not set'
        if not cls.com.is_open:
            cls.com.open()
            ret = func(cls, *args, **kwargs)
            cls.com.close()
        else:
            ret = func(cls, *args, **kwargs)
        return ret
    return _do

class device(object):
    com = None
    product_information = None

    def __init__(self, communicator=None):
        if communicator is None: return
        self.set_communicator(communicator)
        pass

    def set_communicator(self, communicator):
        self.com = communicator
        self._communication_config()
        return self.com

    def _communication_config(self):
        pass

    @_open_close
    def get_product_information(self):
        pass

    @_open_close
    def reset(self):
        pass


class scpi_device(device):
    @_open_close
    def get_product_information(self):
        self.com.send('*IDN?')
        self.product_information = self.com.recv()
        return self.product_information

    @_open_close
    def reset(self):
        yn = raw_input('Do you reset the product? (y/N)')
        if yn.lower() == 'y':
            self.com.send('*RST')
        return


