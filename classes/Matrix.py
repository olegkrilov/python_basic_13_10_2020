from functools import reduce

from random import randint


class Matrix:

    @classmethod
    def get_as_string(cls, data):
        _str = ''

        for row in data:
            for col in row:
                _str += str(col).rjust(10, ' ')
            _str += '\n'

        return _str

    def __init__(self):
        self.__data = []
        self.__x = 0
        self.__y = 0

    def __str__(self):
        _head = f'Matrix {self.__x} X {self.__y}\n' + ('-' * (self.__x * 10)) + '\n'
        _body = Matrix.get_as_string(self.__data)
        return _head + _body

    def __getitem__(self, search_val):
        if isinstance(search_val, tuple) or isinstance(search_val, list):
            try:
                x, y = search_val
                return self.__data[y][x]

            except IndexError:
                return None

        elif isinstance(search_val, dict):
            try:
                return self.__data[search_val['y']][search_val['x']]

            except IndexError:
                return None

            except KeyError:
                return None

        else:
            return None

    def __add__(self, another_matrix):
        self.__x = max(self.__x, another_matrix.x)
        self.__y = max(self.__y, another_matrix.y)
        _data = []

        _i = 0
        while _i < self.__y:
            row = []
            __i = 0
            while __i < self.__x:
                _val = self[(__i, _i)] or 0
                __val = self[(__i, _i)] or 0
                row.append((self[(__i, _i)] or 0) + (another_matrix[(__i, _i)] or 0))
                __i += 1
            _data.append(row)
            _i += 1

        self.__data = _data

    @property
    def size(self):
        return self.__x, self.__y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def generate_data(self, x=None, y=None):
        if x is None:
            x = randint(2, 5)

        if y is None:
            y = randint(2, 5)

        self.__x = x
        self.__y = y
        self.__data = []

        _i = 0
        while _i < y:
            _data = []
            _i += 1
            __i = 0
            while __i < x:
                __i += 1
                _data.append(randint(-999, 999))

            self.__data.append(_data)

        return self
