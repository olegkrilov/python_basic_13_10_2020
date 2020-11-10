from controllers.AbstractTask import AbstractTask
from classes.WonderfulComplexNumber import WonderfulComplexNumber
from common.utils import (
    clear_screen,
    request_boolean,
    request_from_list
)


class Task7(AbstractTask):

    def __run_calculation(self):
        actions = {
            '+': (lambda a, b: a + b, '+'),
            '-': (lambda a, b: a - b, '-'),
            '*': (lambda a, b: a * b, '*'),
            '/': (lambda a, b: a / b, '/')
        }

        arg_a = WonderfulComplexNumber(input('A = '))
        action = actions[request_from_list(actions.keys(), f'What to do ? [+, -, *, /]')]
        arg_b = WonderfulComplexNumber(input('B = '))

        print(arg_a, action[1], arg_b, '=', action[0](arg_a, arg_b))
        self.is_done = not request_boolean('\nRepeat ? ')

    def run(self):
        clear_screen()
        print(self)
        print('-' * 100)
        self.__run_calculation()
