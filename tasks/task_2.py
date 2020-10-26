from time import (
    sleep
)
from random import (
    randint
)
from bycicles.input_requests import (
    request_boolean
)
from bycicles.helpers import (
    show_data
)


def show_task():
    print('\nTASK # 2')
    print('Представлен список чисел. Необходимо вывести элементы исходного списка,')
    print('значения которых больше предыдущего элемента.\n')


def _generate_seed(length=None):
    if length is None:
        length = randint(10, 20)

    return [randint(1, 999) for _ in range(length)]


def main():
    done = False

    show_task()
    while not done:
        data = _generate_seed()
        derivative_data = [val for index, val in enumerate(data) if index > 0 and val > data[index - 1]]
        show_data(data, 'Original Data')
        sleep(1)
        show_data(derivative_data, 'Derivative data')

        done = not request_boolean('\nRepeat')


if __name__ == '__main__':
    main()
