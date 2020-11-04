from random import (
    randint,
    choice
)
from string import ascii_letters


class Cell:

    __cells = {}

    __slots__ = ('__name', '__cores')

    def __init__(self, name=None, cores=None):
        self.__name = Cell._get_unique_name() if name is None else name
        self.__cores = randint(1, 99) if cores is None else cores
        Cell.__cells[self.__name] = self

    def __str__(self):
        return f'{self.__name} ({self.__cores})\n' + '\n'.join(self.make_order(10)) + '\n'

    def __add__(self, other):
        if isinstance(other, Cell):
            self.cores = self.__cores + other.cores
            other.vanish()

    def __sub__(self, other):
        if isinstance(other, Cell):
            _cores_left = self.__cores - other.cores
            if _cores_left < 0:
                self.vanish()
                other.cores = _cores_left
            elif _cores_left > 0:
                other.vanish()
                self.cores = _cores_left
            else:
                self.vanish()
                other.vanish()

    def __mul__(self, other):
        if isinstance(other, Cell):
            self.cores = self.__cores * other.cores
            other.vanish()

    def __truediv__(self, other):
        if isinstance(other, Cell):
            self.cores = self.__cores // (other.cores or 1)
            other.vanish()

    def vanish(self):
        self.__cores = 0
        del Cell.__cells[self.__name]

    def make_order(self, in_row=10):
        _cores = []
        _len = self.cores

        while _len > 0:
            _cores.append('@' * min(_len, in_row))
            _len -= in_row

        return _cores

    @property
    def name(self):
        return self.__name

    @property
    def cores(self):
        return self.__cores

    @cores.setter
    def cores(self, value):
        try:
            self.__cores = abs(value)
            if not self.__cores:
                self.vanish()

        except ValueError:
            pass

    @classmethod
    def _get_unique_name(cls):
        return ''.join([choice(ascii_letters) for _ in range(10)])

    @classmethod
    def clear_all(cls):
        cls.__cells.clear()

    @classmethod
    def show_all(cls, in_row=5):
        _cells = [(cell.name, cell.cores, cell.make_order()) for _, cell in cls.__cells.items()]
        _len = len(_cells)
        _max_rows = 10
        _i = 0

        def _get_view(val, offset=20):
            return str(val).ljust(offset, ' ')

        if not _len:
            print('[NO CELLS]')
        else:
            while _i < _len:
                __i = _i + in_row
                __cells = _cells[_i: __i]
                __len = min(len(__cells), in_row)
                __max_size = 0

                _str = '\n'
                for _cell in __cells:
                    _str += _get_view(f'{_cell[0]} ({_cell[1]})')
                    __max_size = min(_max_rows, max(__max_size, len(_cell[2])))

                print(_str, end='\n')

                ___i = 0
                while ___i < __max_size:
                    __str = ''

                    for _cell in __cells:
                        try:
                            __str += _get_view(_cell[2][___i])
                        except IndexError:
                            __str += _get_view('')

                    print(__str, end='\n')
                    ___i += 1

                _i = __i

    @classmethod
    def get_number_of_cells(cls):
        return len(cls.__cells.keys())

    @classmethod
    def get_random_cell(cls, exclude=None):
        keys = [_key for _key in filter(
            lambda key: True if exclude is None else exclude != key,
            cls.__cells.keys()
        )]
        cell = cls.__cells[choice(keys)]

        return cell
