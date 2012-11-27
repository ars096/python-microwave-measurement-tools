#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import device

def select_power_meter(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return SCPI_command(*args, **kwargs)
    if command_type=='anritsu': return anritsu_command(*args, **kwargs)
    return None


class power_meter(object):
    """
    Power Meter
    ===========

    使用できるメソッド
    ------------------
    * measure(ch=1)

    * set_average(average, ch=1)
    * set_unit(units, ch=1)

    * check_average(ch=1)
    * check_unit(ch=1)

    * get_product_information()

    使用できるプロパティ
    -------------------
    * tested_products
    """
    def measure(self, ch=1):
        """
        検出された強度を読み取ります。

        Parameters
        ----------
        ch : int
            取得するチャンネル番号を指定します。
            デフォルトは 1

        Returns
        -------
        observed : float
            検出された強度
            単位は、check_unit で確認出来ます。

        Examples
        --------
        >>> pm.measure()
        -21.3
        """
        pass

    def set_average(self, average, ch=1):
        """
        時間平均の回数を指定します。

        Parameters
        ----------
        average : int
            平均回数
        ch : int
            設定するチャンネル番号を指定します。
            デフォルトは 1

        Returns
        -------
        average : int, 設定後の平均回数

        Examples
        --------
        >>> pm.set_average(21)
        21
        """
        pass

    def check_average(self, ch=1):
        """
        時間平均の回数を確認します。

        Parameters
        ----------
        ch : int
            取得するチャンネル番号を指定します。
            デフォルトは 1

        Returns
        -------
        average : int, 平均回数

        Examples
        --------
        >>> pm.check_average()
        21
        """
        pass

    def set_unit(self, units, ch=1):
        """
        取得するデータの単位を指定します。

        Parameters
        ----------
        units : ['dBm', 'W', 'DBUV', 'DBMW']
            取得するデータの単位
        ch : int
            設定するチャンネル番号を指定します。
            デフォルトは 1

        Returns
        -------
        unit : 設定後の単位

        Examples
        --------
        >>> pm.set_unit('dBm')
        'dBm'
        """
        pass

    def check_unit(self, ch=1):
        """
        取得するデータの単位を確認します。

        Parameters
        ----------
        ch : int
            確認するチャンネル番号を指定します。
            デフォルトは 1

        Returns
        -------
        unit : 単位

        Examples
        --------
        >>> pm.check_unit()
        'dBm'
        """
        pass



class anritsu_command(power_meter, device.device):
    tested_products = {
        'Anritsu':[
            'Not Yet',
            ]
    }
    @device._open_close
    def measure(self, ch=1):
        """
        -- Method --
        retrieve a value of power meter
        """
        self.com.send('O %d' %ch)
        return float(self.com.readline())

    #@device._open_close
    def set_average(self, average, ch=1):
        """
        -- Method --
        set average by time
        mode is always 'AUTO'
        """
        #TODO:someday
        if ch == 1: ch = 'A'
        elif ch == 2: ch = 'B'
        self.com.open()
        self.com.send('AVG %s, AUTO, %d'%(ch, average))
        self.com.close()
        import time
        time.sleep(1)
        return self.check_average(ch)

    @device._open_close
    def check_average(self, ch=1):
        """
        -- Method --
        check average by time
        """
        if ch == 1: ch = 'A'
        elif ch == 2: ch = 'B'
        self.com.send('AVG? %s'%ch)
        a = int(self.com.readline().split(',')[-1])
        return a

    @device._open_close
    def check_unit(self, ch=1):
        """
        -- Method --
        check units
        """
        self.com.send('CHUNIT? %d' %ch)
        return self.com.readline().strip().split(',')[-1]

    @device._open_close
    def set_unit(self, units, ch=1):
        """
        -- Method --
        set unit ([dBm] or [W] or [DBUV) or [DBMW]
        """
        self.com.send('CHUNIT %d, %s' %(ch,units))
        return self.check_unit(ch)

    # set doc strings
    __doc__ = power_meter.__doc__
    measure.__doc__ = power_meter.measure.__doc__
    set_average.__doc__ = power_meter.set_average.__doc__
    check_average.__doc__ = power_meter.check_average.__doc__
    set_unit.__doc__ = power_meter.set_unit.__doc__
    check_unit.__doc__ = power_meter.check_unit.__doc__


