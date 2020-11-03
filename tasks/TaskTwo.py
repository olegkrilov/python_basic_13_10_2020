from common.AbstractTask import AbstractTask
from common.utils import request_boolean


class TaskTwo(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'data/TaskTwo.txt'
        self._header = 'Task # 2:'

    def run(self):
        self.show_description()
        self.is_done = not request_boolean('\nRepeat? ')
