from tasks.TaskFive.Stationery import Stationery


class Pencil(Stationery):

    def __init__(self):
        super().__init__('Pencil')
        self._drawing_line = u'\u2582'
