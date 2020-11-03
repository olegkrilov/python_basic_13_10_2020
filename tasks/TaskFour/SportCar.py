from tasks.TaskFour.Car import Car


class SportCar(Car):

    def __init__(self):
        super().__init__('red', 'Dodge Viper')
        self._max_speed = 300
