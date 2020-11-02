

class Road:

    def __init__(self, length, width, mass=25, depth=5):
        self._length = length
        self._width = width
        self._mass = mass
        self._depth = depth

    def calculate(self):
        result = (self._length * 1000) * self._width * self._mass * self._depth

        print(f'\nTo build the road {self._length} kilometers long')
        print(f'and {self._width} meters width')
        print(f'and {self._depth} centimeters depth,')
        print(f'considering weight of asphalt')
        print(f'for 1 square meter x 1 centimeter depth')
        print(f'is equal {self._mass} kilogrammes,')
        print(f'we need {result} kilogrammes of the bitumen.')

        return self
