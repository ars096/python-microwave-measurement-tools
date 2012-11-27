#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import time
import numpy
import device

set_sleep = 0.3

def select_spectrum_analyzer(command_type, *args, **kwargs):
    command_type = command_type.lower()
    if command_type=='scpi': return scpi(*args, **kwargs)
    if command_type=='hp8590': return hp8590(*args, **kwargs)
    #if command_type=='anritsu': return anritsu_command(*args, **kwargs)
    return None

class spectrum_analyzer(object):
    """
    Spectrum Analyzer
    =================

    使用できるメソッド
    ------------------
    * set_freq_center(freq, unit='MHz')
    * set_freq_span(freq, unit='MHz')
    * set_freq_start(freq, unit='MHz')
    * set_freq_stop(freq, unit='MHz')
    * set_average(average_num)
    * set_resolution_bandwidth(bandwidth, unit='MHz')
    * set_sweep_points(points)

    * check_freq_center()
    * check_freq_span()
    * check_freq_start()
    * check_freq_stop()
    * check_average()
    * check_resolution_bandwidth()
    * check_sweep_points()

    * measure()

    * get_axis()
    * get_product_information()

    使用できるプロパティ
    -------------------
    * tested_products
    """
    def get_axis(self):
        """
        取得するスペクトルの横軸を生成します。

        Parameters
        ----------
        None :

        Returns
        -------
        axis : array, トレースの横軸 [Hz]

        Examples
        --------
        >>> sa.get_axis()
        array([ 9.0e+9, ... , 1.1e+10 ])

        """
        start = self.check_freq_start()
        end = self.check_freq_stop()
        num = self.check_sweep_points()
        return numpy.linspace(start, end, num)

    def set_freq_center(self, freq, unit='MHz'):
        """
        中心周波数を設定します。

        Parameters
        ----------
        freq : float
            スペクトルの中心周波数
        unit : ['Hz', 'kHz', 'MHz', GHz']
            freq の単位
            デフォルトは 'MHz'

        Returns
        -------
        freq : 設定後の中心周波数 [Hz]

        Examples
        --------
        >>> sa.set_freq_center(3, 'GHz')
        3000000000.0
        """
        pass

    def check_freq_center(self):
        """
        中心周波数を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        freq : 中心周波数 [Hz]

        Examples
        --------
        >>> sa.check_freq_center()
        3000000000.0
        """
        pass

    def set_freq_start(self, freq, unit='MHz'):
        """
        開始周波数を設定します。

        Parameters
        ----------
        freq : float
            スペクトルの開始周波数
        unit : ['Hz', 'kHz', 'MHz', GHz']
            freq の単位
            デフォルトは 'MHz'

        Returns
        -------
        freq : 設定後の開始周波数 [Hz]

        Examples
        --------
        >>> sa.set_freq_start(2, 'GHz')
        2000000000.0
        """
        pass

    def check_freq_start(self):
        """
        開始周波数を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        freq : 開始周波数 [Hz]

        Examples
        --------
        >>> sa.check_freq_start()
        2000000000.0
        """
        pass

    def set_freq_stop(self, freq, unit='MHz'):
        """
        終了周波数を設定します。

        Parameters
        ----------
        freq : float
            スペクトルの終了周波数
        unit : ['Hz', 'kHz', 'MHz', GHz']
            freq の単位
            デフォルトは 'MHz'

        Returns
        -------
        freq : 設定後の終了周波数 [Hz]

        Examples
        --------
        >>> sa.set_freq_stop(4, 'GHz')
        4000000000.0
        """
        pass

    def check_freq_stop(self):
        """
        終了周波数を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        freq : 終了周波数 [Hz]

        Examples
        --------
        >>> sa.check_freq_stop()
        4000000000.0
        """
        pass

    def set_freq_span(self, freq, unit='MHz'):
        """
        観測する周波数幅を設定します。

        Parameters
        ----------
        freq : float
            スペクトルの周波数幅
        unit : ['Hz', 'kHz', 'MHz', GHz']
            freq の単位
            デフォルトは 'MHz'

        Returns
        -------
        freq : 設定後の周波数幅 [Hz]

        Examples
        --------
        >>> sa.set_freq_span(2, 'GHz')
        2000000000.0
        """
        pass

    def check_freq_span(self):
        """
        観測している周波数幅を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        freq : 周波数幅 [Hz]

        Examples
        --------
        >>> sa.check_freq_span()
        2000000000.0
        """
        pass

    def set_average(self, average_num):
        """
        時間平均の回数を指定します。

        Parameters
        ----------
        average_num : int
            平均回数。0 の場合は average 無し。

        Returns
        -------
        average_num : 設定後の平均回数

        Examples
        --------
        >>> sa.set_average(100)
        100
        """
        pass

    def check_average(self):
        """
        時間平均の回数を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        average_num : int, 平均回数
            0 の場合は average 無し

        Examples
        --------
        >>> sa.check_average()
        0
        """
        pass

    def set_resolution_bandwidth(self, bandwidth, unit='MHz'):
        """
        Resolution Band Width を指定します。

        Parameters
        ----------
        freq : float
            Res. BW の周波数幅
        unit : ['Hz', 'kHz', 'MHz', GHz']
            freq の単位
            デフォルトは 'MHz'

        Returns
        -------
        freq : 設定後の周波数幅 [Hz]

        Examples
        --------
        >>> sa.set_resolution_bandwidth(300, 'kHz')
        300000.0
        """
        pass

    def check_resolution_bandwidth(self):
        """
        Resolution Band Width を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        freq : 周波数幅 [Hz]

        Examples
        --------
        >>> sa.check_resolution_bandwidth()
        300000.0
        """
        pass

    def set_sweep_points(self, points):
        """
        観測する総点数を指定します。

        Parameters
        ----------
        points : int
            スイープする点数

        Returns
        -------
        points : 設定後のスイープ点数

        Examples
        --------
        >>> sa.set_sweep_points(2001)
        2001
        """
        pass

    def check_sweep_points(self):
        """
        観測する総点数を確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        points : スイープ点数

        Examples
        --------
        >>> sa.check_sweep_points()
        2001
        """
        pass

    def set_unit(self, unit):
        pass

    def check_unit(self):
        pass

    def set_yrange(self, yrange):
        pass

    def check_yrange(self):
        pass

    def measure(self):
        """
        トレースされたスペクトルを取得します。

        Parameters
        ----------
        None :

        Returns
        -------
        spectrum : array
            観測されたスペクトル

        Examples
        --------
        >>> sa.measure()
        array([ -7.78900000e+01,  ... , -7.80700000e+01 ])
        """
        pass


class scpi(spectrum_analyzer, device.scpi_device):
    tested_products = {
        'Agilent Technologies':[
            'E4440A, Ethernet(port=5025)',
            ]
    }

    @device._open_close
    def set_freq_center(self, freq, unit='MHz'):
        self.com.send(':FREQ:CENTER %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_center()

    @device._open_close
    def check_freq_center(self):
        self.com.send(':FREQ:CENTER?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_start(self, freq, unit='MHz'):
        self.com.send(':FREQ:START %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_start()

    @device._open_close
    def check_freq_start(self):
        self.com.send(':FREQ:START?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_stop(self, freq, unit='MHz'):
        self.com.send(':FREQ:STOP %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_stop()

    @device._open_close
    def check_freq_stop(self):
        self.com.send(':FREQ:STOP?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_span(self, freq, unit='MHz'):
        self.com.send(':FREQ:SPAN %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_span()

    @device._open_close
    def check_freq_span(self):
        self.com.send(':FREQ:SPAN?')
        return float(self.com.readline())

    @device._open_close
    def check_average(self):
        self.com.send(':AVERAGE?')
        average_onoff = float(self.com.readline())
        if average_onoff==0.: return 0.
        self.com.send(':AVERAGE:COUNT?')
        return float(self.com.readline())

    @device._open_close
    def set_average(self, average_num):
        if average_num==0:
            self.com.send(':AVERAGE OFF')
        else:
            self.com.send(':AVERAGE ON')
            self.com.send(':AVERAGE:COUNT %d'%average_num)
        time.sleep(set_sleep)
        return float(self.check_average())

    @device._open_close
    def check_resolution_bandwidth(self):
        self.com.send(':BANDWIDTH:RESOLUTION:AUTO?')
        auto = float(self.com.readline())
        if auto==1.: return -1.
        self.com.send(':BANDWIDTH:RESOLUTION?')
        return float(self.com.readline())

    @device._open_close
    def set_resolution_bandwidth(self, bandwidth, unit='MHz'):
        if bandwidth=='auto':
            self.com.send(':BANDWIDTH:RESOLUTION:AUTO ON')
            return float(self.check_resolution_bandwidth())
        self.com.send(':BANDWIDTH:RESOLUTION %f %s'%(bandwidth, unit))
        return float(self.check_resolution_bandwidth())

    @device._open_close
    def set_sweep_points(self, points):
        self.com.send(':SENSE:SWEEP:POINTS %d'%(points))
        return self.check_sweep_points()

    @device._open_close
    def check_sweep_points(self):
        self.com.send(':SENSE:SWEEP:POINTS?')
        return int(self.com.readline())

    @device._open_close
    def measure(self):
        self.com.send(':TRACE:DATA? TRACE1')
        spectrum_str = self.com.readline()
        spectrum = numpy.array(spectrum_str.split(','), dtype=float)
        return spectrum

    # set doc strings
    __doc__ = spectrum_analyzer.__doc__
    set_freq_center.__doc__ = spectrum_analyzer.set_freq_center.__doc__
    check_freq_center.__doc__ = spectrum_analyzer.check_freq_center.__doc__
    set_freq_start.__doc__ = spectrum_analyzer.set_freq_start.__doc__
    check_freq_start.__doc__ = spectrum_analyzer.check_freq_start.__doc__
    set_freq_stop.__doc__ = spectrum_analyzer.set_freq_stop.__doc__
    check_freq_stop.__doc__ = spectrum_analyzer.check_freq_stop.__doc__
    set_freq_span.__doc__ = spectrum_analyzer.set_freq_span.__doc__
    check_freq_span.__doc__ = spectrum_analyzer.check_freq_span.__doc__
    set_average.__doc__ = spectrum_analyzer.set_average.__doc__
    check_average.__doc__ = spectrum_analyzer.check_average.__doc__
    set_resolution_bandwidth.__doc__ = spectrum_analyzer.set_resolution_bandwidth.__doc__
    check_resolution_bandwidth.__doc__ = spectrum_analyzer.check_resolution_bandwidth.__doc__
    set_sweep_points.__doc__ = spectrum_analyzer.set_sweep_points.__doc__
    check_sweep_points.__doc__ = spectrum_analyzer.check_sweep_points.__doc__
    measure.__doc__ = spectrum_analyzer.measure.__doc__


class hp8590(spectrum_analyzer, device.device):
    tested_products = {
        'Agilent Technologies':[
            '8596E, GPIB',
            ]
    }

    @device._open_close
    def get_product_information(self):
        self.com.send('ID?')
        id = self.com.readline()
        self.com.send('SER?')
        ser = self.com.readline()
        self.com.send('REV?')
        rev = self.com.readline()
        idn =  'Agilent Technologies, %s, %s, %s'%(id.strip(),
                                                   ser.strip(),
                                                   rev)
        self.product_information = idn
        return self.product_information

    @device._open_close
    def set_freq_center(self, freq, unit='MHz'):
        self.com.send('CF %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_center()

    @device._open_close
    def check_freq_center(self):
        self.com.send('CF?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_start(self, freq, unit='MHz'):
        self.com.send('FA %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_start()

    @device._open_close
    def check_freq_start(self):
        self.com.send('FA?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_stop(self, freq, unit='MHz'):
        self.com.send('FB %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_stop()

    @device._open_close
    def check_freq_stop(self):
        self.com.send('FB?')
        return float(self.com.readline())

    @device._open_close
    def set_freq_span(self, freq, unit='MHz'):
        self.com.send('SP %f %s'%(freq, unit))
        time.sleep(set_sleep)
        return self.check_freq_span()

    @device._open_close
    def check_freq_span(self):
        self.com.send('SP?')
        return float(self.com.readline())

    @device._open_close
    def check_average(self):
        self.com.send('VAVG?')
        return float(self.com.readline())

    @device._open_close
    def set_average(self, average_num):
        if average_num==0:
            self.com.send('VAVG OFF')
        else:
            self.com.send('VAVG ON')
            self.com.send('VAVG %d'%average_num)
        time.sleep(set_sleep)
        return float(self.check_average())

    @device._open_close
    def check_resolution_bandwidth(self):
        self.com.send('RB?')
        return float(self.com.readline())

    @device._open_close
    def set_resolution_bandwidth(self, bandwidth, unit='MHz'):
        if bandwidth=='auto':
            self.com.send('RB AUTO')
            return float(self.check_resolution_bandwidth())
        self.com.send('RB %f %s'%(bandwidth, unit))
        return float(self.check_resolution_bandwidth())

    @device._open_close
    def set_sweep_points(self, points):
        return self.check_sweep_points

    @device._open_close
    def check_sweep_points(self):
        return 401

    @device._open_close
    def measure(self):
        self.com.send('TRA?')
        spectrum_str = self.com.readline()
        spectrum = numpy.array(spectrum_str.split(','), dtype=float)
        return spectrum

    # set doc strings
    __doc__ = spectrum_analyzer.__doc__
    set_freq_center.__doc__ = spectrum_analyzer.set_freq_center.__doc__
    check_freq_center.__doc__ = spectrum_analyzer.check_freq_center.__doc__
    set_freq_start.__doc__ = spectrum_analyzer.set_freq_start.__doc__
    check_freq_start.__doc__ = spectrum_analyzer.check_freq_start.__doc__
    set_freq_stop.__doc__ = spectrum_analyzer.set_freq_stop.__doc__
    check_freq_stop.__doc__ = spectrum_analyzer.check_freq_stop.__doc__
    set_freq_span.__doc__ = spectrum_analyzer.set_freq_span.__doc__
    check_freq_span.__doc__ = spectrum_analyzer.check_freq_span.__doc__
    set_average.__doc__ = spectrum_analyzer.set_average.__doc__
    check_average.__doc__ = spectrum_analyzer.check_average.__doc__
    set_resolution_bandwidth.__doc__ = spectrum_analyzer.set_resolution_bandwidth.__doc__
    check_resolution_bandwidth.__doc__ = spectrum_analyzer.check_resolution_bandwidth.__doc__
    set_sweep_points.__doc__ = spectrum_analyzer.set_sweep_points.__doc__
    check_sweep_points.__doc__ = spectrum_analyzer.check_sweep_points.__doc__
    measure.__doc__ = spectrum_analyzer.measure.__doc__

