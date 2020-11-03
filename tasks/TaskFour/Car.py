from time import sleep

from common.utils import (
    clear_screen,
    as_function
)

from tasks.TaskFour.Speedometer import Speedometer


class Car:

    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self._max_speed = 10
        self.__speedometer = Speedometer()
        self.__is_banned = False

    def __refresh_view(self, direction='-----GoGoGo!!!-----'):
        clear_screen()
        if self.speed > self._max_speed or self.is_banned:
            if self.is_police:
                print('We are chasing someone!')
                print('Wiu-Wiu-Wiu!!!')
            else:
                self.is_banned = True
                print('Engine overheat!!!')

        print(f'Driving {self.name}')
        print(direction)
        self.__speedometer.show_speed(self.speed)

    def go(self):
        self.speed += 3
        self.__refresh_view()
        return self

    def stop(self):
        while self.speed:
            self.speed -= 1
            self.__refresh_view('-------Break-------')
            sleep(.1)

        return self

    def turn(self, direction):
        _str = f'Turning {direction}'
        next_speed = self.speed - 3
        if next_speed < 0:
            next_speed = 1

        self.speed = next_speed
        self.__refresh_view(as_function(_str.ljust if direction == 'left' else _str.rjust, 19, ' '))
        return self

    @property
    def is_banned(self):
        return self.__is_banned

    @is_banned.setter
    def is_banned(self, state):
        if state and not self.is_police:
            self.__is_banned = True
