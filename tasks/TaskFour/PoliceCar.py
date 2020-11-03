from tasks.TaskFour.Car import Car


class PoliceCar(Car):

    def __init__(self):
        super().__init__('white', 'Toyota Prius', True)
        self._max_speed = 60
