from common.utils import (
    request_boolean,
    clear_screen,
    as_function
)

from tasks.AbstractTask import AbstractTask

from tasks.TaskThree.Position import Position


class TaskThree(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'tasks/TaskThree/TaskThree.txt'
        self._header = 'Task # 3'
        self.workers = []
        with open('tasks/TaskThree/Workers.txt', 'r', encoding='utf-8') as workers_list:
            self.__prepare_data(workers_list.read())

    def __prepare_data(self, workers_list):
        def _get_datum(_str):
            _datum = _str.split(':')
            _names = _datum[0].strip().split(' ')

            return Position(_names[0], _names[1], _datum[1].strip())

        self.workers = [_get_datum(_str) for _str in workers_list.split('\n')]

    def __get_cell(self, _val, size, align='left', is_currency=False):
        _str = str(f'${round(_val, 2)}' if is_currency else _val)
        return as_function(_str.ljust if align == 'left' else _str.rjust, size, ' ')

    def __draw_as_grid(self, columns, rows):
        grid_header = ''
        grid_body = ('-' * 90) + '\n'

        for key, val in columns.items():
            grid_header += val['label']

        for row in rows:
            for key, val in columns.items():
                grid_body += val['value'](row)

            grid_body += '\n'

        print(grid_header)
        print(grid_body)

    def __show_full_list(self):
        print('List of the registered workers:')

        self.__draw_as_grid(
            {
                'name': {
                    'label': self.__get_cell('Name', 15),
                    'value': lambda datum: self.__get_cell(datum['name'], 15)
                },
                'surname': {
                    'label': self.__get_cell('Surname', 15),
                    'value': lambda datum: self.__get_cell(datum['surname'], 15)
                },
                'position': {
                    'label': self.__get_cell('Surname', 40),
                    'value': lambda datum: self.__get_cell(datum['position'], 40)
                },
                'wage': {
                    'label': self.__get_cell('Surname', 10, 'right'),
                    'value': lambda datum: self.__get_cell(datum['wage'], 10, 'right', True)
                },
                'bonus': {
                    'label': self.__get_cell('Surname', 10, 'right'),
                    'value': lambda datum: self.__get_cell(datum['bonus'], 10, 'right', True)
                }
            },
            [_worker.get_full_data() for _worker in self.workers]
        )

    def __show_compiled_list(self):
        print('\nList of total incomes:')

        self.__draw_as_grid(
            {
                'name': {
                    'label': self.__get_cell('Full name', 50),
                    'value': lambda datum: self.__get_cell(datum.get_full_name(), 50)
                },
                'bonus': {
                    'label': self.__get_cell('Total income', 40, 'right'),
                    'value': lambda datum: self.__get_cell(datum.get_total_income(), 40, 'right', True)
                }
            },
            [worker for worker in self.workers]
        )

    def run(self):
        clear_screen()
        self.show_description()
        self.__show_full_list()
        self.__show_compiled_list()
        self.is_done = not request_boolean('\nRepeat ?')
