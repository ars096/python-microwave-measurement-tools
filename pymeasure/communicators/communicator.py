#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Documents
"""

class communicator(object):
    """
    """
    type = ''
    timeout = None  # in seconds
    default_recv_byte = 100
    default_sending_term_char = '\n'
    buffer = ''
    is_open = False

    def _get_communication_instance(self):
        pass

    def open(self):
        if self.is_open: return self._get_communication_instance()
        ret = self._open()
        self.is_open = True
        return ret

    def _open(self):
        pass

    def close(self):
        if not self.is_open: return None
        ret = self._close()
        self.is_open = False
        return ret

    def _close(self):
        pass

    def set_timeout(self, sec):
        pass

    def set_default_sending_term_char(self, term_char):
        self.default_sending_term_char = term_char

    def set_default_recv_byte(self, byte):
        self.default_recv_byte = byte

    def recv(self, byte=0, *args, **kwargs):
        if byte==0: byte = self.default_recv_byte
        return self._recv(byte, *args, **kwargs)

    def _recv(self, byte, *args, **kwargs):
        pass

    def send(self, msg, term_char=None, *args, **kwargs):
        if term_char is None: term_char = self.default_sending_term_char
        return self._send(msg+term_char, *args, **kwargs)

    def _send(self, msg, *args, **kwargs):
        pass

    def readline(self, term_char='\n'):
        """
        """
        import time
        while True:
            recvd = self.recv()
            separated = recvd.split(term_char)
            if len(separated)==1:
                self.buffer += recvd
            elif len(separated)==2:
                ret = self.buffer + separated[0] + term_char
                self.buffer = separated[1]
                break
            else:
                print('error')
                ret = self.buffer + recvd
                self.buffer = ''
                break
            time.sleep(1/100.)
            continue
        return ret
