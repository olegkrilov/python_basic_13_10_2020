from common.utils import (
    request_from_list,
    clear_screen
)

from tasks.AbstractTask import AbstractTask

from tasks.TaskOne.TrafficLight import TrafficLight


class TaskOne(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'tasks/TaskOne/TaskOne.txt'
        self._header = 'Task # 1'
        self.trafficLight = TrafficLight()

    def __select_mode(self):
        modes = {
            's': 'standard',
            'i': 'idle',
            'd': 'disco',
            'q': None
        }

        print('Select TrafficLight Mode or [Q] to quit:')
        print('-' * 40)
        for key, val in modes.items():
            print(f'[{key.upper()}]:', f'Run in {val} mode' if val else 'Quit')

        selected_mode = modes[request_from_list([key for key in modes.keys()], ' ')]

        if selected_mode is None:
            self.is_done = True

        return selected_mode

    def run(self):
        clear_screen()
        self.show_description()
        mode = self.__select_mode()

        if mode:
            with open(f'tasks/TaskOne/{mode}.mode', 'r', encoding='utf-8') as schedule:
                self.trafficLight.run(schedule.read())
