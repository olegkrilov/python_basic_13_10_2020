from homeworks.les_1.utils import any_key, request_int, request_bool, get_with_padding

print('Task #2')
print('2. Пользователь вводит время в секундах. Переведите время в часы,')
print('минуты и секунды и выведите в формате чч:мм:сс. Используйте')
print('форматирование строк.\n')

done = False

any_key()

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
