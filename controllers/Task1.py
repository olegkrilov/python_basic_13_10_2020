from controllers.AbstractTask import AbstractTask
from classes.AwesomeDateParser import AwesomeDateParser
from common.utils import (
    request_boolean,
    clear_screen
)


class Task1(AbstractTask):

    def __init__(self):
        super().__init__()
        self.__core = AwesomeDateParser()

    def run(self):
        clear_screen()
        print(self)
        self.__core.date = input('Input date\nRequired format is [MM-DD-YYYY]\n>>> ')
        print(self.__core)

        self.is_done = not request_boolean('\nTry again ?')
