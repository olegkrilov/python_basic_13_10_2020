from common.utils import (
    clear_screen,
    request_boolean
)
from abc import abstractmethod


class AbstractTask:

    def __init__(self):
        self.__is_done = False
        self.__name = self.__class__.__name__
        self.__description = None

    def __str__(self):
        def _get_description():
            return ''.join([(_str + '\n') for _str in (['\n'] + self.__description.split('\n') + ['\n'])])

        if self.__description:
            return _get_description()
        else:
            with open(f'data/{self.__name}.txt', 'r', encoding='utf-8') as task_description:
                self.__description = f'{self.__name}:\n{task_description.read()}'
                return _get_description()

    def __call__(self):
        self.init()

    def init(self):
        while not self.is_done:
            self.run()

        return self

    @abstractmethod
    def run(self):
        clear_screen()
        print(self)
        self.is_done = not request_boolean('\nRepeat? ')

    @property
    def is_done(self):
        return self.__is_done

    @is_done.setter
    def is_done(self, state=None):
        self.__is_done = not self.__is_done if state is None else bool(state)

