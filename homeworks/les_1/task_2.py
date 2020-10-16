print('Task #2')
print('2. Пользователь вводит время в секундах. Переведите время в часы,')
print('минуты и секунды и выведите в формате чч:мм:сс. Используйте')
print('форматирование строк.\n')


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


def get_with_padding(some_val, padding_symbol='0', length=2):
    return str(some_val).rjust(length, padding_symbol)


any_key()
done = False
while not done:

    time_in_seconds = request_int('Input time in seconds >>> ', 'Integers! We need INTEGERS!!!')

    seconds_in_minute = 60
    minutes_in_hour = 60
    seconds_in_hour = seconds_in_minute * minutes_in_hour

    seconds = int(time_in_seconds % seconds_in_minute)
    minutes = int(((time_in_seconds - seconds) / seconds_in_minute) % minutes_in_hour)
    hours = int(time_in_seconds // seconds_in_hour)

    print(get_with_padding(hours), get_with_padding(minutes), get_with_padding(seconds), sep=':')
    print('\n')

    if request_bool('Do you want to repeat? >>> '):
        done = False
    else:
        done = True
