# from random import (
#     choice,
#     randint
# )

from bycicles.input_requests import (
    request_boolean
)

from bycicles.helpers import (
    clear_screen
)

TARGET_FILE = 'task_3.txt'
SPACE_KEY = ' '


def show_task():
    print('\nTASK # 3')
    print('Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.')
    print('Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.')
    print('Выполнить подсчет средней величины дохода сотрудников.\n')


# def _generate_data():
#     data = ''
#     random_first_names = ['Ivan', 'Stepan', 'Fedor', 'Petr', 'Denis']
#     random_last_names = ['off', 'chuk', 'enko', 'in']
#
#     _i = 0
#     while _i < 10:
#         data += (choice(random_first_names) + ' '
#                  + choice(random_first_names) + choice(random_last_names) + ' '
#                  + str(randint(17, 25) * 1000)
#                  + '\n')
#         _i += 1
#
#     with open(f'files/{TARGET_FILE}', 'w', encoding='utf-8') as file:
#         file.write(data)
#         file.close()
#
#     print(data)

def get_users_data(data):
    threshold = 2 * (10 ** 4)

    def _get_user(_str):
        _datum = _str.split(SPACE_KEY)
        _salary = float(_datum[2])

        return {
            'name': _datum[0] + ', ' + _datum[1],
            'salary': _salary,
            'rate': _salary < threshold
        }

    return [_get_user(_str) for _str in data if _str and len(_str)]


def show_users_data(data):
    columns = {
        'Name': lambda _datum: _datum['name'],
        'Rate': lambda _datum: '+' if _datum['rate'] else '-',
        'Salary': lambda _datum: _datum['salary']
    }
    grid_header = ''
    grid_body = ('-' * 70) + '\n'
    grid_footer = '\r\r' + ('-' * 70) + '\n'
    total = 0
    good_employees = []
    bad_employees = []

    def _draw_cell(_col, _str):
        return str(_str).ljust(30, ' ') if _col == 'Name' else str(_str).rjust(20, ' ')

    for column_name in columns:
        grid_header += _draw_cell(column_name, column_name)

    for datum in data:
        for column_name, get_value in columns.items():
            grid_body += _draw_cell(column_name, get_value(datum))
        grid_body += '\n'
        total += datum['salary']
        (good_employees if datum['rate'] else bad_employees).append(datum['name'])

    grid_footer += (f'Average Salary: {total / len(data)}'.rjust(70) + '\n')
    grid_footer += (f'Total Salary: {total}'.rjust(70) + '\n')

    print(grid_header)
    print(grid_body)
    print(grid_footer)

    print('\nGood Employees (that know that money is the piece of Evil):\n' + ('-' * 70))
    for _name in good_employees:
        print(_name)

    print('\nGreedy Employees (fire\'em all!):\n' + ('-' * 70))
    for _name in bad_employees:
        print(_name)


def main():
    done = False

    clear_screen()
    show_task()
    while not done:
        with open(f'files/{TARGET_FILE}', 'r', encoding='utf-8') as file:
            data = get_users_data([_str for _str in file.read().split('\n')])
            show_users_data(data)
            file.close()

        done = not request_boolean('\nRepeat ?')


if __name__ == '__main__':
    main()

