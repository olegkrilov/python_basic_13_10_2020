from itertools import (
    count,
    cycle
)
from bycicles.input_requests import (
    request_number,
    request_from_list
)
from bycicles.helpers import (
    show_data,
    generate_seed
)


def show_task():
    print('\nTASK # 6')
    print('Реализовать два небольших скрипта:')
    print('а) итератор, генерирующий целые числа, начиная с указанного,')
    print('б) итератор, повторяющий элементы некоторого списка, определенного заранее.\n')


def _select_generator():

    def _integer_generator():
        val = request_number('Input start point (int):')
        print(f'Start from {val}')
        return count(val)

    def _array_repeat_script():
        data = generate_seed(length=5)
        print(f'\nOriginal data:\n{data}')
        return cycle(data)

    _generators = {
        'I': {
            'label': 'Integer Generator script',
            'get_generator': _integer_generator
        },
        'R': {
            'label': 'Predefined Array Repeat script',
            'get_generator': _array_repeat_script
        },
        'Q': {
            'label': 'Quit',
            'get_generator': None
        }
    }
    _keys = []
    _msg = '\nSelect:\n' + ('-' * 42) + '\n'

    for key, value in _generators.items():
        _keys.append(key.lower())
        _msg += f'[{key}]: {value["label"]}\n'

    return _generators[request_from_list(
        _keys,
        _msg
    ).upper()]


def main():
    done = False

    show_task()
    while not done:
        user_choice = _select_generator()

        if callable(user_choice['get_generator']):
            _generator = user_choice['get_generator']()
            show_data([next(_generator) for _ in range(12)], user_choice['label'])
        else:
            done = True


if __name__ == '__main__':
    main()
