from common.AbstractTask import AbstractTask
from common.utils import (
    request_boolean,
    request_number,
    request_from_list,
)
from classes.Cloth import (
    Suit,
    Coat
)


class TaskTwo(AbstractTask):

    def __init__(self):
        super().__init__()
        self._description_source = 'data/TaskTwo.txt'
        self._header = 'Task # 2:'

    def __select_cloth(self):
        clothes = {
            's': ('Sue a suit', 'stature', Suit),
            'c': ('Sue a coat', 'size', Coat),
            'q': ('Quit', None)
        }

        print('Select Cloth or [Q] to quit:')
        print('-' * 40)
        for key, val in clothes.items():
            print(f'[{key.upper()}]:', f'{val[0]}')

        selected_cloth = clothes[request_from_list([key for key in clothes.keys()], '\n')]

        if selected_cloth[1] is None:
            self.is_done = True

        else:
            message, key, constructor = selected_cloth
            size = request_number(f'Input {key} (sm):')
            cloth = constructor(size)

            print(
                f'To {str(message).lower()} with {key} = {size} sm' +
                f' need {cloth.tissue_consumption} square sm of the tissue.\n'
            )

        return self

    def run(self):
        self.show_description()
        self.__select_cloth()

        if not self.is_done:
            self.is_done = not request_boolean('\nRepeat? ')
