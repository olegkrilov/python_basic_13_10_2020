from tasks.TaskFour.Car import Car


class WorkCar(Car):

    def __init__(self):
        super().__init__('green', 'Mann')
        self._max_speed = 40
