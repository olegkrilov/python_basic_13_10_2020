from controllers.AbstractTask import AbstractTask
from classes.IncredibleNumberStorage import IncredibleNumberStorage
from common.utils import (
    request_boolean,
    clear_screen
)


class Task3(AbstractTask):

    def __init__(self):
        super().__init__()
        self.__core = IncredibleNumberStorage()

    def __action(self):
        _res = self.__core()

        print('\nIncredibleNumberStorage contains:')
        print(_res)

    def run(self):
        clear_screen()
        print(self)
        self.__action()

        self.is_done = not request_boolean('\nRepeat ?')
