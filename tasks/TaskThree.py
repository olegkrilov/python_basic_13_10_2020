from common.AbstractTask import AbstractTask
from common.utils import request_boolean


class TaskThree(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'data/TaskThree.txt'
        self._header = 'Task # 3:'

    def run(self):
        self.show_description()
        self.is_done = not request_boolean('\nRepeat? ')
