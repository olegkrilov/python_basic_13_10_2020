from controllers.AbstractTask import AbstractTask
from classes.UltimateZeroDivisionException import UltimateZeroDivisionException
from common.utils import (
    request_boolean,
    request_number,
    clear_screen
)


class Task2(AbstractTask):

    def __init__(self):
        super().__init__()
        self.__zeroDivisionException = UltimateZeroDivisionException

    def __try_to_divide(self):
        _divider = request_number('Divider')
        _denominator = request_number('Denominator')

        try:
            print(f'{_divider} / {_denominator} = {_divider / _denominator}')

        except ZeroDivisionError:
            try:
                raise self.__zeroDivisionException()

            except UltimateZeroDivisionException as err:
                print(err)

    def run(self):
        clear_screen()
        print(self)
        self.__try_to_divide()
        self.is_done = not request_boolean('\nRepeat ?')
