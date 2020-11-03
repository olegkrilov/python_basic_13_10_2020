from tasks.TaskFive.Stationery import Stationery


class Pen(Stationery):

    def __init__(self):
        super().__init__('Pen')
        self._drawing_line = u'\u2581'
