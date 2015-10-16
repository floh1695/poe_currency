#!/usr/bin/python2

class Currency:
    def __init__(self,
                 value,
                 name_s='',
                 name_l=''):
        return

    def set_value(self, value):
        self.value = float(value)

    def get_value(self):
        return self.value

    def __float__(self):
        return float(self.get_value())

    def __add__(self, other):
        return float(self) + float(other)

    def __sub__(self, other):
        return float(self) - float(other)

    def __mul__(self, other):
        return float(self) * float(other)

    def __div__(self, other):
        return float(self) / float(other)

scroll_fragment = Currency(1,                   'Sf' , 'Scroll Fragment')
scroll_wisdom   = Currency(scroll_fragment * 5, 'SoW', 'Scroll of Wisdom')
scroll_portal   = Currency(scroll_wisdom   * 3, 'Ps' , 'Portal Scroll')
