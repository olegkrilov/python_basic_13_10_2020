print('4. Пользователь вводит целое положительное число. Найдите самую')
print('большую цифру в числе. Для решения используйте цикл while и')
print('арифметические операции.\n')


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

    user_input = str(request_int('Give me a number - BIG number, please >>> '))
    max_val = 0
    i = 0
    str_len = len(user_input)

    while i < str_len:
        max_val = max(int(user_input[i]), max_val)
        i += 1

    print(f'\n\nMax value in {user_input} is {max_val}')

    if request_bool('\nDo you want to repeat? >>> '):
        done = False
    else:
        done = True
