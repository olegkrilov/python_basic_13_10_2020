print('6. Спортсмен занимается ежедневными пробежками. В первый день его')
print('результат составил a километров. Каждый день спортсмен увеличивал')
print('результат на 10 % относительно предыдущего. Требуется определить ')
print('номер дня, на который общий результат спортсмена составить не менее b')
print('километров. Программа должна принимать значения параметров a и b и')
print('выводить одно натуральное число — номер дня.\n')


def any_key(custom_str='start'):
    input(f'press any key to {custom_str}\n')


def request_int(message='', error_message='Should be a number!'):

    try:
        return int(input(message))

    except ValueError as err:
        print(error_message or err)
        return request_int(message)


def request_greater_int(threshold=0, message='', error_message='Should be a number!'):
    numb = request_int(message, error_message)

    if numb < threshold:
        print(f'Value should be greater then {threshold}')
        return request_greater_int(threshold, message, error_message)
    else:
        return numb


def request_bool(message='', error_message='Should be Y or N\n'):
    user_input = input(message).lower()

    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print(error_message)
        return request_bool(message, error_message)


def print_intermediate_result(day, val):
    print(f'Day {day}: {val:0.2f} Km')


done = False
any_key()
while not done:

    current_result = request_int('Input CURRENT result (Km) >>> ')
    target_result = request_greater_int(
        current_result,
        f'Input TARGET result (should be greater then {current_result:0.2f} Km) >>> '
    )
    reached_result = current_result
    step = 1.1
    training_day = 1

    print('\n')

    while reached_result < target_result:
        print_intermediate_result(training_day, reached_result)
        training_day += 1
        reached_result *= step

    print_intermediate_result(training_day, reached_result)
    print(f'\nRequired result will be reached in {training_day} day(s)')

    if request_bool('\nDo you want to repeat? >>> '):
        done = False
    else:
        done = True
