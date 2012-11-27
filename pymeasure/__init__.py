#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
pymeasure
=========

目的
  1. 電波計測機器を python から操作します。

使い方 (Signal Generator の例)
-------------------------------
1. デバイスを生成します。
  >>> sg = pymeasure.signalgenerator('SCPI', 'Ethernet',
                                     host='192.168.100.10', port=5025)

2. デバイスに命令を出します。
  >>> sg.set_freq(10, 'GHz')
  >>> sg.set_power(-15, 'dBm')
  >>> sg.output_on()

3. より詳しく使い方を見たい場合は
  >>> help(sg)

デバイスの生成方法
------------------
デバイスを生成するために以下のコマンドを実行します。
  >>> pymeasure.デバイスの種類(コマンドの種類, 通信方法, [通信方法の設定])

使用できるデバイスの種類一覧 (2012/11/27更新)
---------------------------------------------
実装済みのコマンドの種類を併記
* signalgenerator
  - scpi, anritsu, phasematrix

* spectrumanalyzet
  - scpi, hp8590

* powermeter
  - anritsu

* io
  - ni_daq (windows only)

* coaxialswitch
  - agilent11713b, agilent11713c

* attenuator
  - elva1

使用できる通信方法の一覧 (2012/11/27更新)
---------------------------------------
必要な通信方法の設定パラメータを併記
* Ethernet
  - host(ホスト名), port(ポート番号)

* GPIB (via Prologix Ethernet converter)
  - host(ホスト名), port(ポート番号), gpib(GPIBアドレス)

* USB (for National Instruments DAQ, windows only)
  - devname(デバイス名)

Author
------
Atsushi Nishimura (s_a.nishimura@p.s.osakafu-u.ac.jp)
"""

import communicators
import devices

def create_communicator(communication_method, *args, **kwargs):
    """
    通信インスタンスを生成します。

    Parameters
    ----------
    communication_method : 文字列
        'Ethernet', 'LAN' --> Ethernet通信インスタンスを返します。
            必要な引数 : host, port
        'GPIB_Prologix', 'Prologix' --> GPIB_Prologix通信インスタンスを返します。
            必要な引数 : host, port, gpib
        'NI_USB' --> NI_DAQ用のUSB通信インスタンスを返します。
            必要な引数 : devname

        文字列の大文字小文字は区別しません。

    Returns
    -------
    com : 通信インスタンス

    Notes
    -----

    Examples
    --------
    >>> com = pymeasure.create_communicator('Ethernet',
                                            host='192.168.100.11', port=5025)
    """
    method = communication_method.lower()

    if method in ['ethernet', 'lan']:
        return communicators.ethernet(*args, **kwargs)

    elif method in ['gpib_prologix', 'gpib-prologix', 'prologix']:
        return communicators.gpib_prologix(*args, **kwargs)

    elif method in ['ni_usb']:
        return communicators.ni_usb(*args, **kwargs)

    return None


def signalgenerator(command_type, communication_method, *args, **kwargs):
    """
    Signal Generator に接続し、使用できるようにします。

    Parameters
    ----------
    command_type : 文字列
        制御コマンドの種類を指定します。
        'SCPI', 'anritsu', 'phasematrix' が使用可能です。
        - 個々のコマンドを用いて利用できる装置名は help(sg) で確認できます。
        command_type の文字列は大文字小文字を区別されません。
    communication_method : 文字列
        通信方式を指定します。
        'Ethernet', 'GPIB_Prologix' が使用可能です。
        - 'Ethernet' の場合、さらに、host, port を引数で与えてください。
        - 'GPIB_Prologix' の場合、さらに、host, port, gpib を引数で与えてください。
        通信方式の引数についての詳細は、pymeasure.create_communicator を
        参照してください。
        communication_method の文字列は大文字小文字を区別されません。

    Returns
    -------
    sg : Signal Generator インスタンス

    Examples
    --------
    >>> sg = pymeasure.signalgenerator('SCPI', 'Ethernet',
                                       host='192.168.100.10', port=5025)
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.signal_generator(command_type, com)

def powermeter(command_type, communication_method, *args, **kwargs):
    """
    Power Meter に接続し、使用できるようにします。

    Parameters
    ----------
    command_type : 文字列
        制御コマンドの種類を指定します。
        'anritsu' が使用可能です。
        - 個々のコマンドを用いて利用できる装置名は help(pm) で確認できます。
        command_type の文字列は大文字小文字を区別されません。
    communication_method : 文字列
        通信方式を指定します。
        'Ethernet', 'GPIB_Prologix' が使用可能です。
        - 'Ethernet' の場合、さらに、host, port を引数で与えてください。
        - 'GPIB_Prologix' の場合、さらに、host, port, gpib を引数で与えてください。
        通信方式の引数についての詳細は、pymeasure.create_communicator を
        参照してください。
        communication_method の文字列は大文字小文字を区別されません。

    Returns
    -------
    pm : Power Meter インスタンス

    Examples
    --------
    >>> pm = pymeasure.powermeter('Anritsu', 'GPIB_Prologix',
                                  host='192.168.100.10', port=1234, gpib=10)
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.power_meter(command_type, com)

def spectrumanalyzer(command_type, communication_method, *args, **kwargs):
    """
    Spectrum Analyzer に接続し、使用できるようにします。

    Parameters
    ----------
    command_type : 文字列
        制御コマンドの種類を指定します。
        'scpi', 'hp8590' が使用可能です。
        - 個々のコマンドを用いて利用できる装置名は help(sa) で確認できます。
        command_type の文字列は大文字小文字を区別されません。
    communication_method : 文字列
        通信方式を指定します。
        'Ethernet', 'GPIB_Prologix' が使用可能です。
        - 'Ethernet' の場合、さらに、host, port を引数で与えてください。
        - 'GPIB_Prologix' の場合、さらに、host, port, gpib を引数で与えてください。
        通信方式の引数についての詳細は、pymeasure.create_communicator を
        参照してください。
        communication_method の文字列は大文字小文字を区別されません。

    Returns
    -------
    sa : Spectrum Analyzer インスタンス

    Examples
    --------
    >>> sa = pymeasure.spectrumanalyzer('SCPI', 'Ethernet',
                                        host='192.168.100.10', port=1234)
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.spectrum_analyzer(command_type, com)

def io(command_type, communication_method, *args, **kwargs):
    """
    (Analog, Digital)I/O に接続し、使用できるようにします。

    Parameters
    ----------
    command_type : 文字列
        制御コマンドの種類を指定します。
        'ni_daq' が使用可能です。
        - 個々のコマンドを用いて利用できる装置名は help(io) で確認できます。
        command_type の文字列は大文字小文字を区別されません。
    communication_method : 文字列
        通信方式を指定します。
        'NI_USB' が使用可能です。
        - 'NI_USB' の場合、さらに、devname を引数で与えてください。
        通信方式の引数についての詳細は、pymeasure.create_communicator を
        参照してください。
        communication_method の文字列は大文字小文字を区別されません。

    Returns
    -------
    io : I/O インスタンス

    Examples
    --------
    >>> io = pymeasure.io('NI_DAQ', 'NI_USB', devname='Dev1')
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.io(command_type, com)

def coaxial_switch(command_type, communication_method, *args, **kwargs):
    """
    Coaxial Switch に接続し、使用できるようにします。

    Parameters
    ----------
    command_type : 文字列
        制御コマンドの種類を指定します。
        'agilent11713b', 'agilent11713c' が使用可能です。
        - 個々のコマンドを用いて利用できる装置名は help(cs) で確認できます。
        command_type の文字列は大文字小文字を区別されません。
    communication_method : 文字列
        通信方式を指定します。
        'Ethernet', 'GPIB_Prologix' が使用可能です。
        - 'Ethernet' の場合、さらに、host, port を引数で与えてください。
        - 'GPIB_Prologix' の場合、さらに、host, port, gpib を引数で与えてください。
        通信方式の引数についての詳細は、pymeasure.create_communicator を
        参照してください。
        communication_method の文字列は大文字小文字を区別されません。

    Returns
    -------
    cs : Coaxial Switch インスタンス

    Examples
    --------
    >>> cs = pymeasure.coaxialswitch('Agilent11713C', 'Ethernet',
                                     host='192.168.100.10', port=5025)
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.coaxial_switch(command_type, com)

def attenuator(command_type, communication_method, *args, **kwargs):
    """
    Attenuator に接続し、使用できるようにします。

    Parameters
    ----------
    command_type : 文字列
        制御コマンドの種類を指定します。
        'elva1' が使用可能です。
        - 個々のコマンドを用いて利用できる装置名は help(att) で確認できます。
        command_type の文字列は大文字小文字を区別されません。
    communication_method : 文字列
        通信方式を指定します。
        'GPIB_Prologix' が使用可能です。
        - 'GPIB_Prologix' の場合、さらに、host, port, gpib を引数で与えてください。
        通信方式の引数についての詳細は、pymeasure.create_communicator を
        参照してください。
        communication_method の文字列は大文字小文字を区別されません。

    Returns
    -------
    att : Attenuator インスタンス

    Examples
    --------
    >>> att = pymeasure.attenuator('ELVA1', 'GPIB_Prologix',
                                   host='192.168.100.10', port=1234, gpib=4)
    """
    com = create_communicator(communication_method, *args, **kwargs)
    return devices.attenuator(command_type, com)


