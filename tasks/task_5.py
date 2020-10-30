from functools import (
    reduce
)

from time import (
    sleep
)

from bycicles.input_requests import (
    request_boolean
)

from bycicles.helpers import (
    clear_screen,
    print_link_to_file,
    generate_seed
)

SPACE_KEY = ' '


def show_task():
    print('\nTASK # 5')
    print('Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.')
    print('Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.\n')


def _generate_data():
    _i = 0

    while _i < 30:
        print(f'Generating data.{"." * (_i % 4)}{" " * (4 - (_i % 4))}', end='\r')
        sleep(.1)
        _i += 1

    return SPACE_KEY.join([str(val) for val in generate_seed(length=50)])


def main():
    done = False

    while not done:
        clear_screen()
        show_task()

        file_name = (input('\nInput file name >>> ') or 'task_5') + '.txt'

        with open(f'files/{file_name}', 'w', encoding='utf-8') as file:
            file.write(_generate_data())

        with open(f'files/{file_name}', 'r', encoding='utf-8') as file:
            values = [int(val) for val in file.read().split(SPACE_KEY)]
            print('\nFrom data:\n')
            print(values)
            print(f'\nTotal Sum = {reduce(lambda val, agg: agg + val, values)}')
            print(f'\nLink to file: {file_name}')
            print_link_to_file(file)

        done = not request_boolean('\n\nRepeat ?')


if __name__ == '__main__':
    main()

