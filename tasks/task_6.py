import json

from functools import (
    reduce
)

from bycicles.input_requests import (
    request_boolean
)

from bycicles.helpers import (
    clear_screen,
    as_function,
    print_link_to_file
)

SOURCE_FILE = 'task_6_source'
TARGET_FILE = 'task_6_target'


def show_task():
    print('\nTASK # 6')
    print('Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет')
    print('и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.')
    print('Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,')
    print('содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.\n')


def show_data(data):
    lesson_types = ['Lecture', 'Seminar', 'Workshop']
    grid_header = ''
    grid_body = ('-' * 80) + '\n'

    def _get_cell(_col, _val):
        _str = str(_val if _val else '-')
        return as_function(_str.ljust if _col == 'Name' else _str.rjust, 16, ' ')

    def _get_value(_datum, _prop):
        return _datum[_prop] if _prop in _datum else 0

    columns = {
        'Name': lambda _datum: _datum['name'],
        'Lectures': lambda _datum: _get_value(_datum, lesson_types[0]),
        'Seminars': lambda _datum: _get_value(_datum, lesson_types[1]),
        'Workshops': lambda _datum: _get_value(_datum, lesson_types[2]),
        'Total': lambda _datum: _datum['total']
    }

    for column_name in columns:
        grid_header += _get_cell(column_name, column_name)

    for key, datum in data.items():
        datum['name'] = key
        datum['total'] = reduce(
            lambda val, agg: val + agg,
            [_get_value(datum, lesson_type) for lesson_type in lesson_types]
        )

        for column_name, get_value in columns.items():
            grid_body += _get_cell(column_name, get_value(datum))

        grid_body += '\n'

    print(grid_header)
    print(grid_body)


def main():
    done = False

    while not done:
        clear_screen()
        show_task()

        with open(f'files/{SOURCE_FILE}.json', 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
            show_data(data)

            with open(
                f'files/{input("Input file name to save Data: >>> ") or TARGET_FILE}.json',
                'w', encoding='utf-8'
            ) as _file:
                content = {_key: _val['total'] for _key, _val in data.items()}
                _file.write(json.dumps(content))
                print(f'\n\nLink to file: {_file.name}')
                print_link_to_file(_file)

        done = not request_boolean('\nRepeat ?')


if __name__ == '__main__':
    main()

