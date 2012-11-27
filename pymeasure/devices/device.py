#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import functools

def _open_close(func):
    @functools.wraps(func)
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
        """
        通信クラスをセットします。

        Parameters
        ----------
        communicator : 通信インスタンス
            pymeasure.create_communicator() で生成される通信インスタンスを
            用意してください。

        Returns
        -------
        com : 通信インスタンス
            セットされた通信インスタンスを返します(確認用)

        See Also
        --------
        create_communicator

        Notes
        -----

        Examples
        --------
        >>> com = pymeasure.create_communicator('Ethernet',
                                                host='192.168.0.10', port=1234)
        >>> dev.set_communicator(com)
        <pymeasure.communicators.com_ethernet.ethernet at 0x109992410>
        """
        self.com = communicator
        self._communication_config()
        return self.com

    def _communication_config(self):
        pass

    @_open_close
    def get_product_information(self):
        """
        機器固有の情報(メーカー,型番,シリアル,バージョン,等)を取得します。

        Parameters
        ----------
        None :

        Returns
        -------
        information : 機器固有の情報(メーカー,型番,シリアル,バージョン,等)

        See Also
        --------

        Notes
        -----

        Examples
        --------
        >>> sg.product_information()
        'Agilent Technologies, E8247C, MY00000000, A.00.00\\n'
        """
        pass

    @_open_close
    def reset(self):
        """
        リセットコマンドを送信します。
        (注意：未実装の事があります)

        Examples
        --------
        >>> dev.reset()

        """
        pass


class scpi_device(device):
    @_open_close
    def get_product_information(self):
        self.com.send('*IDN?')
        self.product_information = self.com.recv()
        return self.product_information

    get_product_information.__doc__ = device.get_product_information.__doc__

    @_open_close
    def reset(self):
        yn = raw_input('Do you reset the product? (y/N)')
        if yn.lower() == 'y':
            self.com.send('*RST')
        return

    reset.__doc__ = device.reset.__doc__


