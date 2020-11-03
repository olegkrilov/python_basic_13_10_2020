from tasks.TaskThree.Worker import Worker


class Position(Worker):

    def get_full_name(self):
        return f'{self._name}, {self._surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def get_full_data(self):
        return {
            'name': self._name,
            'surname': self._surname,
            'position': self._position,
            'wage': self._income['wage'],
            'bonus': self._income['bonus']
        }
