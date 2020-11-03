from tasks.TaskFour.Car import Car


class TownCar(Car):

    def __init__(self):
        super().__init__('grey', 'Mitsubishi Lancer 9')
        self._max_speed = 60
