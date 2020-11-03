from random import randint

from time import sleep

from common.utils import (
    request_boolean,
    clear_screen,
    request_from_list
)

from tasks.AbstractTask import AbstractTask

from tasks.TaskFour.TownCar import TownCar
from tasks.TaskFour.SportCar import SportCar
from tasks.TaskFour.WorkCar import WorkCar
from tasks.TaskFour.PoliceCar import PoliceCar


class TaskFour(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'tasks/TaskFour/TaskFour.txt'
        self._header = 'Task # 4'
        self.__selected_car = None

    def __select_car(self):
        cars = {
            'c': ('Town Car', TownCar),
            's': ('Sport Car', SportCar),
            'w': ('Work Car', WorkCar),
            'p': ('Police Car', PoliceCar),
            'q': ('Quit', lambda: None)
        }

        print('Select Car from the list or [Q] to quit:')
        print('-' * 40)
        for key, val in cars.items():
            print(f'[{key.upper()}]:', f'{val[0]}')

        self.__selected_car = cars[request_from_list([key for key in cars.keys()], ' ')][1]()

        if self.__selected_car is None:
            self.is_done = True

        return self

    def __drive(self):
        try:
            while not self.__selected_car.is_banned:
                next_action = randint(0, 10)

                if self.__selected_car.speed < 15:
                    self.__selected_car.go()
                else:
                    if next_action == 0:
                        self.__selected_car.turn('left')
                    elif next_action == 1:
                        self.__selected_car.turn('right')
                    else:
                        self.__selected_car.go()

                sleep(.5)
            else:
                self.__selected_car.stop()

        except KeyboardInterrupt:
            self.__selected_car.stop()

        return self

    def run(self):
        clear_screen()
        self.show_description()
        self.__select_car()
        self.__drive()

        if not self.is_done:
            self.is_done = not request_boolean('\nRepeat ?')

