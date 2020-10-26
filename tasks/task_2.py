from time import (
    sleep
)
from random import (
    choice,
    randint,
    uniform
)
from bycicles.input_requests import (
    request_boolean,
    request_number,
    request_from_list
)


def show_task():
    print('\nTASK # 2')
    print('Представлен список чисел. Необходимо вывести элементы исходного списка,')
    print('значения которых больше предыдущего элемента.\n')


def _generate_seed(length=None):
    if length is None:
        length = randint(10, 20)

    return [randint(1, 999) for val in range(length)]


def _show_data(data, label):
    length = len(data)
    last_index = length - 1
    msg = '['
    print(f'\n{label}\n' + ('-' * 80))

    for index, val in enumerate(data):
        msg += str(val) + (', ' if index < last_index else '')
        print(str(msg).ljust(80, ' '), end='\r')
        sleep(.1)

    print(msg, ']', end='\n')


def main():
    done = False

    show_task()
    while not done:
        data = _generate_seed()
        derivative_data = [val for index, val in enumerate(data) if index > 0 and val > data[index - 1]]
        _show_data(data, 'Original Data')
        sleep(1)
        _show_data(derivative_data, 'Derivative data')

        done = not request_boolean('\nRepeat')


if __name__ == '__main__':
    main()
