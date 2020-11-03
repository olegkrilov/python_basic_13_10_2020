from abc import ABC, abstractmethod
from common.utils import (
    request_boolean,
    clear_screen
)


class AbstractTask(ABC):

    def __init__(self):
        self.__is_done = False
        self._description_source = 'data/AbstractTask.txt'
        self._header = 'Abstract Task:'
        self._description = ''

    def show_description(self):
        def _show_description():
            clear_screen()
            [print(_str) for _str in (['\n'] + self._description.split('\n') + ['\n'])]

        if self._description:
            _show_description()
        else:
            with open(self._description_source, 'r', encoding='utf-8') as task_description:
                self._description = f'{self._header}\n{task_description.read()}'
                _show_description()

        return self

    def init(self):
        while not self.is_done:
            self.run()

        return self

    @abstractmethod
    def run(self):
        self.show_description()
        self.is_done = not request_boolean('\nRepeat? ')

    @property
    def is_done(self):
        return self.__is_done

    @is_done.setter
    def is_done(self, state=None):
        self.__is_done = not self.__is_done if state is None else bool(state)
