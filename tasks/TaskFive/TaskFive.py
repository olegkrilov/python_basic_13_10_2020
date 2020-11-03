from common.utils import (
    request_boolean,
    clear_screen,
    request_from_list
)

from tasks.AbstractTask import AbstractTask
from tasks.TaskFive.Pen import Pen
from tasks.TaskFive.Pencil import Pencil
from tasks.TaskFive.Marker import Marker


class TaskFive(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'tasks/TaskFive/TaskFive.txt'
        self._header = 'Task # 5'
        self.__tool = None

    def __select_tool(self):
        tools = {
            'p': ('Pen', Pen),
            'c': ('Pencil', Pencil),
            'm': ('Marker', Marker),
            'q': ('Quit', lambda: None)
        }

        print('Select Drawing Tool or [Q] to quit:')
        print('-' * 40)
        for key, val in tools.items():
            print(f'[{key.upper()}]:', f'{val[0]}')

        self.__tool = tools[request_from_list([key for key in tools.keys()], ' ')][1]()

        if self.__tool is None:
            self.is_done = True

        return self

    def run(self):
        clear_screen()
        self.show_description()

        self.__select_tool()

        if self.__tool:
            self.__tool.draw()

        if not self.is_done:
            self.is_done = not request_boolean('\n\nRepeat ?')

