from time import sleep
from itertools import cycle
from common.utils import clear_screen


DURATION = 'duration'
COLOR = 'color'
RED = 'r'
YELLOW = 'y'
GREEN = 'g'
COLORS = {
    RED: '\33[91m',
    YELLOW: '\33[93m',
    GREEN: '\33[92m'
}
DEFAULT_COLOR = '\033[0m'


class TrafficLight:

    def __init__(self):
        self.__lights = {_key: {
            COLOR: _val,
            DURATION: 0
        } for _key, _val in COLORS.items()}
        self.__is_running = False

    def __iterate(self, tasks_list):
        _iterable = cycle(tasks_list)

        try:
            while self.__is_running:
                _task = next(_iterable)
                _duration = _task[DURATION]

                for _key in [_key for _key in _task.keys() if _key != DURATION]:
                    if _key in self.__lights:
                        self.__lights[_key][DURATION] = _task[_key]

                while _duration:
                    _duration -= 1
                    self.__show()
                    print('\n[Ctrl + C] to stop')
                    sleep(.5)

        except KeyboardInterrupt:
            self.__is_running = False
            print('Done')

        return self

    def __show(self):
        clear_screen()
        print('Traffic Light, ver 0.0.1')
        for _light in self.__lights.values():
            __light_on = _light[COLOR] + (u'\u2593' * 2) + DEFAULT_COLOR
            __light_off = (u'\u2591' * 2)
            if _light[DURATION]:
                print(__light_on)
                _light[DURATION] -= 1
            else:
                print(__light_off)
        return self

    def run(self, schedule):
        _done = False
        _tasks_list = []

        for _str in schedule.split('\n'):
            _task = {
                DURATION: 0
            }
            for __str in _str.split(','):
                _subtask = __str.split(':')
                _subtask_key = _subtask[0]
                _subtask_duration = int(_subtask[1])
                _task[_subtask_key] = _subtask_duration
                _task[DURATION] = _task[DURATION] if _subtask_duration < _task[DURATION] else _subtask_duration

            _tasks_list.append(_task)

        self.__is_running = True

        return self.__iterate(_tasks_list)
