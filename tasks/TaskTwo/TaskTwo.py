from common.utils import (
    request_number,
    request_boolean,
    clear_screen
)

from tasks.AbstractTask import AbstractTask

from tasks.TaskTwo.Road import Road


class TaskTwo(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'tasks/TaskTwo/TaskTwo.txt'
        self._header = 'Task # 2'

    def run(self):
        clear_screen()
        self.show_description()

        road = Road(
            request_number('Input Road length (km)'),
            request_number('Input Road width (m)')
        )

        road.calculate()

        self.is_done = not request_boolean('\nRepeat?')
