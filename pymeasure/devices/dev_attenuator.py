#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_attenuator(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return SCPI(*args, **kwargs)
    if command_type in ['elva1', 'elva-1']:
        return elva1(*args, **kwargs)
    return None


class attenuator(object):
    """
    Attenuator
    ==========

    使用できるメソッド
    ------------------
    * set_level(level)
    * check_level()

    * get_product_information()

    使用できるプロパティ
    -------------------
    * tested_products
    """
    def set_level(self, level):
        """
        アッテネータのレベルを設定します。

        Parameters
        ----------
        level : float
            設定するレベル

        Returns
        -------
        level : float, 設定後のレベル

        Examples
        --------
        >>> att.set_level(20)
        20
        """
        pass

    def check_level(self):
        """
        アッテネータのレベルを確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        level : float, レベル

        Examples
        --------
        >>> att.check_level()
        20
        """
        pass


class elva1(attenuator, device.scpi_device):
    """
    ELVA1
    =====

    使用できるメソッド
    ------------------
    * set_gpib_address(gpib)

    """
    tested_products = {
        'ELVA1':[
            'GPDVC-15/100/RS, GPIB',
            ]
    }

    level = None

    def check_level(self):
        return self.level

    @device._open_close
    def set_level(self, level=0):
        self.com.send('PO %04X'%int(level))
        self.level = int(level)
        return self.check_level()

    @device._open_close
    def get_gpib_address(self):
        self.com.send('SYST:COMM:GPIB:ADDR?')
        return int(self.com.readline())

    @device._open_close
    def set_gpib_address(self, gpib):
        """
        GPIBアドレスを設定します。

        Parameters
        ----------
        gpib : int
            設定するGPIBアドレス

        Returns
        -------
        gpib : int, 設定後のGPIBアドレス

        Examples
        --------
        >>> att.set_gpib_address(21)
        21
        """
        self.com.send('SYST:COMM:GPIB:ADDR %d'%gpib)
        self.com.set_gpib_address(gpib)
        self.com.send('*SAV 0')
        return self.get_gpib_address()

    # set doc strings
    __doc__ = attenuator.__doc__
    set_level.__doc__ = attenuator.set_level.__doc__
    check_level.__doc__ = attenuator.check_level.__doc__
