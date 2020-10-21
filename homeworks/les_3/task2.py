import re

print('\n2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:')
print('имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры,')
print('как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.\n')


def request_bool(message=''):
    choice = str(input(f'{message} (y / n)? >>> ')).lower()
    if choice in ['y', 'n']:
        return choice == 'y'
    else:
        print('Type Y or N')
        return request_bool(message)


def request_string(message='', pattern='', is_required=True):
    _str = str(input(f'{message} >>> ')).strip()
    _pattern = re.compile(pattern) if pattern else None

    if is_required and not _str:
        print('ERROR: Is required!')
        return request_string(message, pattern, is_required)

    elif _pattern and not _pattern.match(_str):
        print('ERROR: Wrong format!')
        return request_string(message, pattern, is_required)

    else:
        return _str


def create_user(**kwargs):
    user_data = {}

    for key, val in kwargs.items():
        user_data[key] = val

    return user_data


done = False
while not done:
    print('\nUser data:\n', create_user(
        first_name=request_string(
            'Input first name               '),
        last_name=request_string(
            'Input last name                '),
        year_of_birth=request_string(
            'Input year (4 digits)          ', '^\d{4}$'),
        city=request_string(
            'Input city                     '),
        email=request_string(
            'Email (should be a valid email)', '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'),
        phone=request_string(
            'Phone (should be a valid phone)', '^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$')
    ))

    done = not request_bool('\nDo you want to repeat')
