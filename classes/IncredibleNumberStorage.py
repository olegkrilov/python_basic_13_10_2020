from common.utils import clear_screen
from time import sleep


class NumbersOnlyException(Exception):

    def __init__(self, message='Should be a number!'):
        self.message = message

    def __str__(self):
        return self.message


class IncredibleNumberStorage:

    __DEFAULT_STOP_CODE = 'DONE'

    def __init__(
            self,
            message='Input Some Lovely Number \n(ThisOne prefers Numbers rather then Chars)',
            error_message='Should be a NUMBER, YOU MORON!!! NUMBER!!!!!',
            stop_code=__DEFAULT_STOP_CODE
    ):
        self.__is_done = True
        self.__storage = []
        self.__message = message
        self.__error_message = error_message
        self.__stop_code = stop_code

    def __str__(self):
        _i = 0
        _str = ''
        _len = len(self.__storage)
        _step = 10

        while _i < _len:
            _str += ''.join([str(val).ljust(10, ' ') for val in self.__storage[_i: _i + _step]])
            _str += '\n'
            _i += _step

        return _str if _len else ''

    def __call__(self):
        self.__is_done = False
        self.__storage.clear()

        _message = f'{self.__message}\nInput "{self.__stop_code}" when done\n\n'
        _stop_code = self.__stop_code.lower()

        while not self.is_done:
            clear_screen()
            print(self)
            print(_message)
            user_val = input('>>> ')

            if user_val.lower() != _stop_code:
                try:
                    self.__storage.append(int(user_val))
                except ValueError:
                    try:
                        raise NumbersOnlyException(self.__error_message)
                    except NumbersOnlyException as err:
                        clear_screen()
                        print(self)
                        print(_message)
                        print(f'>>> {user_val} is not a Number, {err}', end='\r\r')
                        sleep(2)
            else:
                self.__is_done = True
                return self.__storage[0:]

    @property
    def is_done(self):
        return self.__is_done
