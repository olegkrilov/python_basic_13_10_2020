class Worker:

    __registered_workers = []

    __salaries = {
        'Cleaning Service Supervisor Assistant': 1500,
        'Senior Penguinologist': 2000,
        'Main Hall Door Opener': 2300,
        'Boobies Expert': 2800,
        'Collegiate Assessor': 3000,
        'Dead Santa': 3400,
        'Other': 1000
    }

    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = self.__get_income_by_position(position)
        self.__registered_workers.append(self)

    def __get_income_by_position(self, position):
        wage = self.__salaries[position if position in self.__salaries else 'Other']
        return {
            'wage': wage,
            'bonus': wage * .25
        }
