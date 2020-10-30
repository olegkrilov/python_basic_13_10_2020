import json

from bycicles.input_requests import (
    request_boolean
)

from bycicles.helpers import (
    clear_screen,
    as_function,
    print_link_to_file
)

SOURCE_FILE = 'task_7_source'
TARGET_FILE = 'task_7_target'
NEW_LINE_KEY = '\n'
SPACE_KEY = ' '


def show_task():
    print('\nTASK # 7')
    print('Создать (не программно) текстовый файл, в котором каждая строка должна содержать')
    print('данные о фирме: название, форма собственности, выручка, издержки.')
    print('Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.')
    print('Если фирма получила убытки, в расчет средней прибыли ее не включать.')
    print('Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, ')
    print('а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь')
    print('(со значением убытков). Итоговый список сохранить в виде json-объекта в соответствующий файл.\n')


def read_and_show_source_data(source):
    keys = ['Name', 'Type', 'Profit', 'Loss']

    def _get_datum(_str):
        _datum = {
            keys[_i]: (float(_val) if keys[_i] in ['Profit', 'Loss'] else _val)
            for _i, _val in enumerate(_str.split(SPACE_KEY))
        }

        _datum['Total'] = _datum['Profit'] - _datum['Loss']

        return _datum

    def _get_cell(_prop, _val):
        __str = str(_val)
        _is_text_field = _prop == 'Name' or _prop == 'Type'
        _size = 20 if _is_text_field else 16

        return as_function(__str.ljust if _is_text_field else __str.rjust, _size, ' ')

    data = [_get_datum(_str) for _str in source.split(NEW_LINE_KEY)]
    total_profit = 0
    average_profit = 0
    profitable_companies_number = 0

    columns = {_key: _key for _key in (keys + ['Total'])}
    grid_header = ''
    grid_body = ('-' * 88) + '\n'

    for column_name in columns:
        grid_header += _get_cell(column_name, column_name)

    for datum in data:
        if datum['Total'] > 0:
            total_profit += datum['Total']
            profitable_companies_number += 1

        for column_name, get_value in columns.items():
            grid_body += _get_cell(column_name, datum[column_name])

        grid_body += '\n'

    average_profit += total_profit / (profitable_companies_number or 1)

    print(grid_header)
    print(grid_body)

    return data, average_profit


def main():
    done = False

    while not done:
        clear_screen()
        show_task()

        with open(f'files/{SOURCE_FILE}.txt', 'r', encoding='utf-8') as source_file:
            data, average_profit = read_and_show_source_data(source_file.read())

            with open(
                f'files/{input("Input file name to save Data: >>> ") or TARGET_FILE}.json',
                'w', encoding='utf-8'
            ) as target_file:
                content = [
                    {datum['Name']: datum['Total'] for datum in data},
                    {'average_profit': average_profit}
                ]
                target_file.write(json.dumps(content))
                print(f'\n\nLink to file: {target_file.name}')
                print_link_to_file(target_file)

        done = not request_boolean('\nRepeat ?')


if __name__ == '__main__':
    main()

