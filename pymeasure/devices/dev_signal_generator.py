#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import time
import device

def select_signal_generator(command_type, *args, **kwargs):
    command_type = command_type.lower()
    if command_type=='scpi': return scpi(*args, **kwargs)
    if command_type=='anritsu': return anritsu(*args, **kwargs)
    if command_type=='phasematrix': return phasematrix(*args, **kwargs)
    return None

class signal_generator(object):
    """
    Signal Generator
    ================

    使用できるメソッド
    ------------------
    * set_freq(freq, unit='MHz')
    * set_power(power, unit='dBm')
    * output_on()
    * output_off()
    * check_freq()
    * check_power()
    * check_output()
    * get_product_information()

    使用できるプロパティ
    -------------------
    * tested_products
    """
    def set_freq(self, freq, unit='MHz'):
        """
        出力する RF 周波数を設定します。

        Parameters
        ----------
        freq : float
            出力する RF 周波数
        unit : ['Hz', 'kHz', 'MHz', 'GHz']
            freq の単位
            デフォルトは 'MHz'

        Returns
        -------
        freq : 設定後の周波数 [Hz]

        Examples
        --------
        >>> sg.set_freq(1000, 'MHz')
        10000000000.0
        """
        pass

    def check_freq(self):
        """
        出力する RF 周波数を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        freq : 出力する RF 周波数 [Hz]

        Examples
        --------
        >>> sg.check_freq()
        10000000000.0
        """
        pass

    def set_power(self, power, unit='dBm'):
        """
        出力する RF 信号強度を設定します。

        Parameters
        ----------
        power : float
            出力する RF 信号強度
        unit : ['dBm']
            power の単位
            デフォルトは 'dBm'

        Returns
        -------
        power : 設定後の出力強度 [dBm]

        Examples
        --------
        >>> sg.set_power(-20)
        -20.0
        """
        pass

    def check_power(self):
        """
        出力する RF 信号強度を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        power : 出力する RF 信号強度 [dBm]

        Examples
        --------
        >>> sg.check_power()
        -20.0
        """
        pass

    def check_output(self):
        """
        RF 信号が出力されているか確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        output : 1 -- ON,  0 -- OFF

        Examples
        --------
        >>> sg.check_output()
        0
        """
        pass

    def output_on(self):
        """
        RF 出力を ON にします。

        Parameters
        ----------
        None :

        Returns
        -------
        output : 1 -- ON,  0 -- OFF

        Examples
        --------
        >>> sg.output_on()
        1
        """
        pass

    def output_off(self):
        """
        RF 出力を OFF にします。

        Parameters
        ----------
        None :

        Returns
        -------
        output : 1 -- ON,  0 -- OFF

        Examples
        --------
        >>> sg.output_off()
        0
        """
        pass


class scpi(signal_generator, device.scpi_device):
    tested_products = {
        'Agilent Technologies':[
            'E8241A, Ethernet(port=7777)',
            'E8247C, Ethernet(port=7777)',
            'E8247A, Ethernet(port=7777)',
            'E8257D, Ethernet(port=7777)',
        ]
    }

    @device._open_close
    def set_freq(self, freq, unit='MHz'):
        self.com.send('FREQ %f %s'%(freq, unit))
        return self.check_freq()

    @device._open_close
    def check_freq(self):
        self.com.send('FREQ?')
        return float(self.com.readline())

    @device._open_close
    def set_power(self, power, unit='dBm'):
        self.com.send('POW %f %s'%(power, unit))
        return self.check_power()

    @device._open_close
    def check_power(self):
        self.com.send('POW?')
        return float(self.com.readline())

    @device._open_close
    def check_output(self):
        self.com.send('OUTP?')
        return int(self.com.readline())

    @device._open_close
    def output_on(self):
        self.com.send('OUTP 1')
        return self.check_output()

    @device._open_close
    def output_off(self):
        self.com.send('OUTP 0')
        return self.check_output()

    # set doc strings
    __doc__ = signal_generator.__doc__
    set_freq.__doc__ = signal_generator.set_freq.__doc__
    check_freq.__doc__ = signal_generator.check_freq.__doc__
    set_power.__doc__ = signal_generator.set_power.__doc__
    check_power.__doc__ = signal_generator.check_power.__doc__
    check_output.__doc__ = signal_generator.check_output.__doc__
    output_on.__doc__ = signal_generator.output_on.__doc__
    output_off.__doc__ = signal_generator.output_off.__doc__


class anritsu(scpi):
    tested_products = {
        'Anritsu':[
            'Not Yet',
        ]
    }
    #TODO: test this class

    @device._open_close
    def set_power(self, power, unit='dBm'):
        self.com.send('AMPL:LEV %f %s'%(power, unit))
        return self.check_power()

    @device._open_close
    def check_power(self):
        self.com.send('AMPL:LEV?')
        return float(self.com.readline())

    @device._open_close
    def check_output(self):
        self.com.send('AMPL:STAT 0')
        return int(self.com.readline())

    @device._open_close
    def output_on(self):
        self.com.send('AMPL:STAT 1')
        return self.check_output()

    @device._open_close
    def output_off(self):
        self.com.send('AMPL:STAT 0')
        return self.check_output()

    # set doc strings
    __doc__ = signal_generator.__doc__
    set_power.__doc__ = signal_generator.set_power.__doc__
    check_power.__doc__ = signal_generator.check_power.__doc__
    check_output.__doc__ = signal_generator.check_output.__doc__
    output_on.__doc__ = signal_generator.output_on.__doc__
    output_off.__doc__ = signal_generator.output_off.__doc__



class phasematrix(signal_generator, device.device):
    tested_products = {
        'Phase Matrix':[
            'FSW-0010, Ethernet(port=10001)'
            ]
    }

    unit_dic = {'GHz': 1e9, 'MHz': 1e6, 'kHz': 1e3}

    def _hex2dn(self, hex_str, byte=4, signed=True):
        if not signed:
            return int(hex_str,16)

        bin_str = bin(int(hex_str,16))[2:]
        if len(bin_str)==(byte*8):
            bin_str = '0'+bin_str
        else:
            format = '%'+'0%d'%(byte*8)+'d'
            bin_str = '1'+format%(int(bin_str))

        complement = '1'+'0'*byte*8
        dn = int(bin_str,2)-int(complement,2)
        return dn

    def _dn2hex(self, dn, byte=4, singned=True):
        format='%'+'0%d'%(byte*2)+'X'
        if not signed:
            return format % dn
        if dn>=0:
            return format % dn
        complement ='1'+'0'*byte*8
        complement_dn = int(complement,2)
        unsigned = complement_dn+dn
        return bin_str

    def _hex2bin(self, hex_str):
        byte = len(hex_str)/2
        bin_str = bin(int(hex_str,16))[2:]
        bin_str = '0'*(byte*8-len(bin_str))+bin_str
        return bin_str

    @device._open_close
    def set_freq(self, freq, unit='MHz'):
        mHz = freq * self.unit_dic[unit] * 1e3
        mHz_hex = '%012X'%int(mHz)
        self.com.send('0C'+mHz_hex)
        return self.check_freq()

    @device._open_close
    def check_freq(self):
        self.com.send('04')
        time.sleep(0.05)
        ret = self.com.recv(14)
        data_bit = self._hex2bin(ret.strip())
        Hz = int(data_bit, 2)/1000.
        return Hz

    @device._open_close
    def set_power(self, dBm, *args, **kwargs):
        tenth_dBm = dBm * 10
        tenth_dBm_hex = ('%04X'%(int('10000',16)+int(tenth_dBm)))[-4:]
        self.com.send('03'+tenth_dBm_hex)
        return self.check_power()

    @device._open_close
    def check_power(self):
        self.com.send('0D')
        time.sleep(0.05)
        ret = self.com.recv(6)
        data_bit = self._hex2bin(ret)
        dBm = int(data_bit, 2)/10
        return dBm

    def check_output(self):
        status = self.get_status()
        return status['RF output']

    @device._open_close
    def output_on(self):
        self.com.send('0F01')
        return self.check_output()

    @device._open_close
    def output_off(self):
        self.com.send('0F00')
        return self.check_output()

    @device._open_close
    def get_product_information(self):
        self.com.send('01')
        time.sleep(0.05)
        ret = self.com.recv(24)
        data_bit = self._hex2bin(ret.strip())
        model = data_bit[:16]
        option = data_bit[16:32]
        soft_ver = data_bit[32:48]
        serial_num = data_bit[48:]
        info = 'Phase Matrix, FSW-0010, %x, %x, %x'%(option, soft_ver, serial_num)
        return info

    @device._open_close
    def get_status(self):
        self.com.send('02')
        time.sleep(0.05)
        ret = self.com.recv(4)
        data_bit = self._hex2bin(ret.strip())
        status = {'Ext Ref': data_bit[-1],
                  'RF unlocked': data_bit[-2],
                  'Ref unlocked': data_bit[-3],
                  'RF output': data_bit[-4],
                  'Voltage Err': data_bit[-5],
                  'Ref outp': data_bit[-6],
                  'Blanking': data_bit[-7],
                  'Lock recovery': data_bit[-8]}
        return status

    # set doc strings
    __doc__ = signal_generator.__doc__
    set_freq.__doc__ = signal_generator.set_freq.__doc__
    check_freq.__doc__ = signal_generator.check_freq.__doc__
    set_power.__doc__ = signal_generator.set_power.__doc__
    check_power.__doc__ = signal_generator.check_power.__doc__
    check_output.__doc__ = signal_generator.check_output.__doc__
    output_on.__doc__ = signal_generator.output_on.__doc__
    output_off.__doc__ = signal_generator.output_off.__doc__
    get_product_information.__doc__ = device.device.get_product_information.__doc__
