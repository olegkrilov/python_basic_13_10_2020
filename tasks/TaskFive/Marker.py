from tasks.TaskFive.Stationery import Stationery


class Marker(Stationery):

    def __init__(self):
        super().__init__('Marker')
        self._drawing_line = u'\u2585'
