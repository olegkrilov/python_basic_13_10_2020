from random import choice
from time import sleep
from classes.Cell import Cell
from common.AbstractTask import AbstractTask
from common.utils import (
    request_boolean,
    clear_screen
)


class TaskThree(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'data/TaskThree.txt'
        self._header = 'Task # 3:'

    def __create_cells(self):
        Cell.clear_all()
        [Cell() for _ in range(10)]
        return self

    def __run_battle_of_cells(self):
        actions = {
            'eat': ('__add__', lambda a, b: a + b),
            'defend from': ('__sub__', lambda a, b: a - b),
            'breed with': ('__mul__', lambda a, b: a * b),
            'remove cores corrupted by': ('__truediv__', lambda a, b: a / b)
        }

        step = 0

        def _print_header():
            clear_screen()
            print(f'ITERATION #{step}')
            print('-' * 100)
            Cell.show_all()
            print('\n')
            print('-' * 100)

        while Cell.get_number_of_cells() > 1:
            _print_header()
            actor = Cell.get_random_cell()
            target = Cell.get_random_cell(actor.name)
            action_key = choice([key for key in actions])
            action = actions[action_key]
            sleep(1)
            print(f'[{actor.name}] is trying to {action_key} [{target.name}] (using {action[0]} protocol)')
            action[1](actor, target)

            _i = 0
            while _i < 35:
                print(f'>Wait{"." * (_i % 4)}{" " * (4 - (_i % 4))}', end='\r')
                _i += 1
                sleep(.1)

            step += 1

        else:
            _print_header()

        return self

    def run(self):
        self.show_description()
        self.__create_cells()
        self.__run_battle_of_cells()
        self.is_done = not request_boolean('\nRepeat? ')
