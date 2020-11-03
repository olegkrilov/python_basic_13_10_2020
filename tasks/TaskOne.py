from random import (randint)

from common.AbstractTask import AbstractTask
from common.utils import (
    request_boolean,
    request_from_list,
    clear_screen
)
from classes.Matrix import Matrix


class TaskOne(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'data/TaskOne.txt'
        self._header = 'Task # 1:'
        self.__matrices = []

    def __generate_matrix(self):
        matrix = Matrix().generate_data()
        self.__matrices.append(matrix)

        self.__select_task(message=f'Matrix created! Total Matrices: {len(self.__matrices)}\n')

    def __show_matrices(self):
        clear_screen()
        print('Existing Matrices:\n')
        [print(matrix) for matrix in self.__matrices]

        self.__select_task(clear=False)

    def __summarize_matrices(self):
        summarized_matrix = Matrix()

        for matrix in self.__matrices:
            summarized_matrix + matrix

        clear_screen()
        print('Summarized Matrix')
        print(summarized_matrix)

        self.__select_task(clear=False)

    def __select_task(self, clear=True, message=None):

        tasks = {
            'c': ('Create New Matrix', lambda: self.__generate_matrix()),
            'e': ('Show existing Matrices', lambda: self.__show_matrices()),
            's': ('Summarize Matrices', lambda: self.__summarize_matrices()),
            'q': ('Quit', None)
        }

        if clear:
            clear_screen()

        if message:
            print(message)

        print('Select Task or [Q] to quit:')
        print('-' * 40)
        for key, val in tasks.items():
            print(f'[{key.upper()}]:', f'{val[0]}')

        selected_task = tasks[request_from_list([key for key in tasks.keys()], ' ')]

        if selected_task[1] is None:
            self.is_done = True

        elif callable(selected_task[1]):
            selected_task[1]()

        return self

    def run(self):
        self.show_description()
        self.__select_task()

        if not self.is_done:
            self.is_done = not request_boolean('\nRepeat? ')
