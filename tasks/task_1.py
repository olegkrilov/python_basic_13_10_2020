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
    print('\nTASK # 1')
    print('Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.')
    print('В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.')
    print('Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.\n')


def _show_employer_data(_employer):
    worked_hours = _employer['worked_days'] * 8
    idle_hours = _employer['idle_days'] * 8

    print(f'\n{_employer["get_full_name"]()}')
    print('-' * 42)
    print(f'      Worked Hours: {worked_hours}')
    print(f'        Idle Hours: {idle_hours}')

    _i = 0
    while _i < _employer['worked_days']:
        print(u'\u2591' * (_i + 1), end='\r')
        sleep(.1)
        _i += 1

    print('\nBonus achieved!' if _employer['bonus_achieved']() else '\n')
    print(f'       Hourly Rate: ${round(_employer["rate"])}')
    print(f'            Salary: ${round(_employer["get_bonus"](), 2)}')
    print(f'             Bonus: ${round(_employer["get_salary"](), 2)}')
    print('-' * 42)
    print(f'             Total: ${round(_employer["get_grand_total"](), 2)}')
    print(('_' * 42) + '\n')


def _show_employers_data(data, columns):
    _grid_header = ''
    _grid_body = ('-' * 90) + '\n'

    def _draw_cell(_col, _str):
        return str(_str).ljust(30, ' ') if _col == 'Name' else str(_str).rjust(20, ' ')

    for column_name in columns:
        _grid_header += _draw_cell(column_name, column_name)

    for datum in data:
        for column_name, get_value in columns.items():
            _grid_body += _draw_cell(column_name, get_value(datum))
        _grid_body += '\n'

    print(_grid_header)
    print(_grid_body)


def _create_employer(
    first_name,
    last_name,
    total_work_days=25,
    min_work_days=17,
    average_hourly_rate=10,
    bonus_threshold=22
):
    worked_days = randint(min_work_days, total_work_days)
    idle_days = total_work_days - worked_days
    rate = average_hourly_rate + ((average_hourly_rate * .3) * uniform(-1, 1))
    employer = {
        'first_name': first_name,
        'last_name': last_name,
        'worked_days': worked_days,
        'idle_days': idle_days,
        'rate': rate,

        'bonus_achieved': lambda: worked_days >= bonus_threshold,
        'get_worked_hours': lambda: worked_days * 8,
        'get_idle_hours': lambda: idle_days * 8,
        'get_full_name': lambda: f'{first_name}, {last_name}',
        'get_bonus': lambda: (worked_days - bonus_threshold) * (8 * rate) if employer['bonus_achieved']() else 0,
        'get_salary': lambda: employer['get_worked_hours']() * rate,
        'get_grand_total': lambda: employer['get_salary']() + employer['get_bonus']()
    }

    return employer


def _generate_seed():
    random_first_names = ['Ivan', 'Stepan', 'Fedor']
    random_last_names = ['off', 'chuk', 'enko']
    employers = []
    total_work_days = 25
    min_work_days = int(total_work_days * .75)
    bonus_threshold = int(total_work_days * .9)

    number_of_employers = request_number('Input number of employers')
    hourly_rate = request_number('Input average hourly rate', get_float=True)

    _i = 0
    while _i < number_of_employers:
        _i += 1
        employers.append(_create_employer(
            choice(random_first_names),
            choice(random_first_names) + choice(random_last_names),
            total_work_days,
            min_work_days,
            hourly_rate,
            bonus_threshold
        ))
        
    _i = 0
    while _i < 10:
        print('Generating seed data' + ('.' * (_i % 5)) + (' ' * (5 - (_i % 5))), end='\r')
        _i += 1
        sleep(.1)

    print('Data generated:                     ', end='\r\n\n')

    return employers


def _request_action():
    def _currency_filter(val):
        return f'${round(val, 2)}'

    _columns = {
        'Name': lambda _datum: _datum['get_full_name'](),
        'Hours Worked': lambda _datum: _datum['get_worked_hours'](),
        'Hours Idle': lambda _datum: _datum['get_idle_hours'](),
        'Hourly Rate': lambda _datum: _currency_filter(_datum['rate']),
        'Salary': lambda _datum: _currency_filter(_datum['get_salary']()),
        'Bonus': lambda _datum: _currency_filter(_datum['get_bonus']()),
        'Total': lambda _datum: _currency_filter(_datum['get_grand_total']())
    }

    _actions = {
        'R': {
            'label': 'Sorted by top hourly rate',
            'key': lambda _datum: _datum['rate'],
            'reverse': True,
            'columns': {
                'Name': _columns['Name'],
                'Hours Worked': _columns['Hours Worked'],
                'Hours Idle': _columns['Hours Idle'],
                'Hourly Rate': _columns['Hourly Rate']
            }
        },
        'S': {
            'label': 'Sorted by top salary',
            'key': lambda _item: _item['get_grand_total'](),
            'reverse': True,
            'columns': {
                'Name': _columns['Name'],
                'Hourly Rate': _columns['Hourly Rate'],
                'Hours Worked': _columns['Hours Worked'],
                'Salary': _columns['Salary']
            }
        },
        'W': {
            'label': 'Sorted by top idle hours',
            'key': lambda _item: _item['idle_days'],
            'reverse': True,
            'columns': {
                'Name': _columns['Name'],
                'Hours Idle': _columns['Hours Idle'],
                'Hours Worked': _columns['Hours Worked'],
                'Bonus': _columns['Bonus'],
            }
        },
        'N': {
            'label': 'Sorted by name',
            'key': lambda _item: _item['get_full_name'](),
            'reverse': False,
            'columns': {
                'Name': _columns['Name'],
                'Salary': _columns['Salary'],
                'Bonus': _columns['Bonus'],
                'Total': _columns['Total'],
            }
        },
        'Q': {
            'label': 'Quit',
            'key': None
        }
    }
    _keys = []
    _msg = 'Select action\n' + ('-' * 42) + '\n'

    for key, value in _actions.items():
        _keys.append(key.lower())
        _msg += f'[{key}]: {value["label"]}\n'

    return _actions[request_from_list(
        _keys,
        _msg
    ).upper()]


def main():
    show_task()

    done = False
    database = _generate_seed()

    while not done:
        action = _request_action()
        if action['key']:
            print('\n' + action['label'])
            database = sorted(database, key=action['key'], reverse=action['reverse'] or False)
            _show_employers_data(database, action['columns'])
            if request_boolean('Do you want to see details'):
                for employer in database:
                    _show_employer_data(employer)
        else:
            done = True


if __name__ == '__main__':
    main()
