print('3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.')
print('Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.\n')


def any_key(custom_str='start'):
    input(f'press any key to {custom_str}\n')


def request_int(message='', error_message='Should be a number!'):

    try:
        return int(input(message))

    except ValueError as err:
        print(error_message or err)
        return request_int(message)


def request_bool(message='', error_message='Should be Y or N\n'):
    user_input = input(message).lower()

    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print(error_message)
        return request_bool(message, error_message)


done = False

any_key()

while not done:
    user_number = request_int('Give me your number >>> ')
    equation_str = ''
    equation_total = 0
    i = 1
    lim = 3

    while i <= lim:
        value_str = str(user_number)
        arg = value_str * i
        equation_total += int(arg)
        i += 1
        equation_str += arg

        if i <= lim:
            equation_str += ' + '

    print(equation_str, equation_total, sep=' = ')

    if request_bool('Do you want to repeat? >>> '):
        done = False
    else:
        done = True
