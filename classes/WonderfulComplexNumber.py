from common.utils import as_function


class WonderfulComplexNumber:

    __DEFAULT_VALUE = '0 + 0j'

    def __init__(self, value=None):
        self.__value = WonderfulComplexNumber.__get_clean(value or WonderfulComplexNumber.__DEFAULT_VALUE)

    def __str__(self):
        return str(self.__value)

    def __call__(self):
        return self.__value

    def __add__(self, other):
        return self.__value + WonderfulComplexNumber.__normalize(other)

    def __mul__(self, other):
        return self.__value * WonderfulComplexNumber.__normalize(other)

    def __sub__(self, other):
        return self.__value - WonderfulComplexNumber.__normalize(other)

    def __truediv__(self, other):
        try:
            self.__value / WonderfulComplexNumber.__normalize(other)
        except ZeroDivisionError:
            print('Do not divide by zero and learn Math, moron.')
            return self.__value

    @property
    def value(self):
        return self()

    @value.setter
    def value(self, _val):
        self.__value = WonderfulComplexNumber.__normalize(_val)

    @staticmethod
    def __get_clean(_val):
        if isinstance(_val, str):
            _val = _val.replace(' ', '')

        try:
            return complex(_val)
        except ValueError:
            print(f'Can\'t create complex number from [{_val}]\nDefault value [0 + 0j] will be applied')
            return complex(WonderfulComplexNumber.__DEFAULT_VALUE)

    @staticmethod
    def __normalize(_val):
        return as_function(_val if isinstance(_val, WonderfulComplexNumber) else WonderfulComplexNumber(_val))
