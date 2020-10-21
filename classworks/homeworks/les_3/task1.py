import time

print('\n1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.')
print('Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.\n')


def lets_divide(numerator, denominator):
    if not denominator:
        print(f'UNCAUGHT ERROR: attempt to divide {numerator} by zero')
        print('Preparing to collapse the Universe...')
        for _i in range(10):
            print(f'{10 - _i}...')
            time.sleep(1)
        else:
            print('The Universe has been collapsed successfully!')
    else:
        return numerator / denominator


def request_bool(message=''):
    choice = str(input(f'{message} (y / n)? >>> ')).lower()
    if choice in ['y', 'n']:
        return choice == 'y'
    else:
        print('Type Y or N')
        return request_bool(message)


def request_number(message=' >>> '):
    try:
        return float(input(message))
    except ValueError:
        print('ValueError: Should be a NUMBER')
        return request_number(message)


def request_denominator():
    choice = request_number('Denominator >>> ')
    if not choice:
        if request_bool('Are your sure, that you want to divide by zero'):
            return choice
        else:
            print('Try again')
            return request_denominator()
    else:
        return choice


done = False
while not done:
    num = request_number('Numerator >>> ')
    den = request_denominator()
    res = lets_divide(num, den)

    if res:
        print(f'\n{num} / {den} = {res}\n')
        done = not request_bool('Do you want to repeat')
    else:
        done = True
