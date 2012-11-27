#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

import numpy
import device

def select_coaxial_switch(command_type, *args, **kwargs):
    command_type = command_type.lower()
    #if command_type=='scpi': return scpi(*args, **kwargs)
    if command_type=='agilent': return agilent(*args, **kwargs)
    if command_type=='agilent11713b': return agilent_11713b(*args, **kwargs)
    if command_type=='agilent11713c': return agilent_11713c(*args, **kwargs)
    return None


class coaxial_switch(object):
    """
    Coaxial Switch
    ==============

    使用できるメソッド
    ------------------
    * set_ch(ch)
    * check_ch()

    * get_product_information()

    使用できるプロパティ
    -------------------
    * tested_products
    """
    def set_ch(self, ch):
        """
        スイッチを接続するチャンネルを設定します。

        Parameters
        ----------
        ch : int
            接続するチャンネル

        Returns
        -------
        ch : list, 設定後の接続チャンネルのリスト

        Examples
        --------
        >>> cs.set_ch(2)
        (2, 2)
        """
        pass

    def check_ch(self):
        """
        スイッチが接続しているチャンネルを確認します。

        Parameters
        ----------
        None :

        Returns
        -------
        ch : list, 設定後の接続チャンネルのリスト

        Examples
        --------
        >>> cs.check_ch()
        (2, 2)
        """
        pass


class agilent(device.scpi_device):
    @device._open_close
    def check_supply_voltage(self, ch=1):
        """
        -- Method --
        query supply voltage to coaxial switch
        """
        self.com.send('CONFigure:BANK%d?' %ch)
        return int(self.com.readline().strip("\n")[1:])

    @device._open_close
    def set_supply_voltage(self, ch=1):
        """
        -- Method --
        set supply voltage to coaxial switch
        note that "Agilent 11713B" sets only supply DC 24V
        """
        self.com.send('CONFigure:BANK%d P24v'%ch)
        return self.check_supply_voltage(ch)

    @device._open_close
    def check_open_switch(self, ch='101:108'):
        """
        -- Method --
        query open switching path.
        """
        self.com.send(':ROUTe:OPEn? (@%s)'%ch)
        return map(int, self.com.readline().strip('\n').split(','))

    @device._open_close
    def check_close_switch(self, ch='101:108'):
        """
        -- Method --
        query close switching path
        """
        self.com.send(':ROUTe:CLOSe? (@%s)'%ch)
        return map(int, self.com.readline().strip('\n').split(','))

    @device._open_close
    def set_open_switch(self, ch='101:104'):
        """
        -- Method --
        set open switching path
        """
        self.com.send(':ROUTe:OPEn (@%s)'%ch)
        return self.check_open_switch(ch)

    @device._open_close
    def set_close_switch(self, ch='101:104'):
        """
        -- Method --
        set close switching path
        """
        self.com.send(':ROUTe:CLOSe (@%s)'%ch)
        return self.check_close_switch(ch)


class agilent_11713b(coaxial_switch, agilent):
    tested_products = {
        'Agilent Technologies':[
            '11713B, GPIB',
            ]
    }

    def check_ch(self):
        getch = lambda x: numpy.where(numpy.array(x)==1)[0][0] + 1
        x1 = getch(self.check_open_switch('101:104'))
        x2 = getch(self.check_open_switch('105:108'))
        return x1, x2

    def set_ch(self, ch):
        if type(ch)==int: ch = [ch]*2
        for ch_num in ch:
            if (ch_num >= 5) or (ch_num <=0):
                print('bad ch number. it must be 1-4')
                return None
            continue

        self.set_close_switch('101:108')
        self.set_open_switch('%d'%(100+ch[1]))
        self.set_open_switch('%d'%(100+ch[1]+4))
        return self.check_ch()

    # set doc strings
    __doc__ = coaxial_switch.__doc__
    set_ch.__doc__ = coaxial_switch.set_ch.__doc__
    check_ch.__doc__ = coaxial_switch.check_ch.__doc__


class agilent_11713c(coaxial_switch, agilent):
    tested_products = {
        'Agilent Technologies':[
            '11713C, Ethernet(port=5025)',
            ]
    }

    def check_ch(self):
        getch = lambda x: numpy.where(numpy.array(x)==1)[0][0] + 1
        x1 = getch(self.check_open_switch('101:104'))
        x2 = getch(self.check_open_switch('105:108'))
        y1 = getch(self.check_open_switch('201:204'))
        y2 = getch(self.check_open_switch('205:208'))
        return x1, x2, y1, y2

    def set_ch(self, ch):
        if type(ch)==int: ch = [ch]*4
        for ch_num in ch:
            if (ch_num >= 5) or (ch_num <=0):
                print('bad ch number. it must be 1-4')
                return None
            continue

        self.set_close_switch('101:108')
        self.set_close_switch('201:208')
        self.set_open_switch('%d'%(100+ch[1]))
        self.set_open_switch('%d'%(100+ch[1]+4))
        self.set_open_switch('%d'%(200+ch[1]))
        self.set_open_switch('%d'%(200+ch[1]+4))
        return self.check_ch()

    # set doc strings
    __doc__ = coaxial_switch.__doc__
    set_ch.__doc__ = coaxial_switch.set_ch.__doc__
    check_ch.__doc__ = coaxial_switch.check_ch.__doc__
