from bycicles.input_requests import (
    request_boolean
)
from bycicles.helpers import (
    show_data
)


def show_task():
    print('\nTASK # 3')
    print('Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.')


def main():
    done = False

    show_task()
    while not done:
        show_data([val for val in range(20, 240) if not (val % 20) or not(val % 21)], 'Range = [20, 240]')

        done = not request_boolean('\nRepeat')


if __name__ == '__main__':
    main()
