from time import sleep


class Stationery:

    __DEFAULT_COLOR = '\033[0m'

    def __init__(self, title):
        self.title = title
        self._drawing_line = '*'

    def draw(self, line_size=100, color='\33[91m'):
        print(f'Let\'s draw with {self.title}!')

        _i = 0
        while _i < line_size:
            _i += 1
            print(f'{(color + self._drawing_line + self.__DEFAULT_COLOR) * _i}' + (' ' * (line_size - _i)), end='\r')
            sleep(.05)



