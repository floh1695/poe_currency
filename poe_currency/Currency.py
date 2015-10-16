#!/usr/bin/python2

class Currency:
    def __init__(self,
                 value,
                 name_s='',
                 name_l=''):
        return

    def set_value(self, value):
        self.value = int(value)

    def get_value(self):
        return self.value

    def __int__(self):
        return self.get_value()
