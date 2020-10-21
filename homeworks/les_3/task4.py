print('\n4. Программа принимает действительное положительное число x и целое отрицательное число y.')
print('Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать')
print('в виде функции my_func(x, y). При решении задания необходимо обойтись')
print('без встроенной функции возведения числа в степень.\n')


def request_bool(message=''):
    choice = str(input(f'{message} (y / n)? >>> ')).lower()
    if choice in ['y', 'n']:
        return choice == 'y'
    else:
        print('Type Y or N')
        return request_bool(message)


def request_number(message='', req_int=False):
    try:
        _val = input(message + ' >>> ')
        return int(_val) if req_int else float(_val)
    except ValueError:
        print('ValueError: Should be a NUMBER')
        return request_number(message, req_int)


def request_positive_natural_number(var_name='X'):
    _val = request_number(f'Input {var_name} (natural, greater then 0)')
    if _val <= 0:
        print('ERROR: Should be greater then 0')
        return request_positive_natural_number(var_name)
    else:
        return _val


def request_negative_integer(var_name='Y'):
    _val = request_number(f'Input {var_name} (integer, less then 0)', req_int=True)
    if _val >= 0:
        print('ERROR: Should be an INTEGER that is less then 0')
        return request_negative_integer(var_name)
    else:
        return _val


def my_func(x, y):
    _x = x
    _y = abs(y)

    while _y - 1:
        _x *= x
        _y -= 1
    else:
        return f'{x} ^ ({y})', 1 / _x


def main():
    done = False

    while not done:
        result = my_func(x=request_positive_natural_number(), y=request_negative_integer())
        print(f'\n{result[0]} = {result[1]}')

        done = not request_bool('\nWould you like to repeat')


main()
