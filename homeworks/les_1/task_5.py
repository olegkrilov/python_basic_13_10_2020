print('5. Запросите у пользователя значения выручки и издержек фирмы.')
print('Определите, с каким финансовым результатом работает фирма (прибыль')
print('— выручка больше издержек, или убыток — издержки больше выручки).')
print('Выведите соответствующее сообщение. Если фирма отработала с')
print('прибылью, вычислите рентабельность выручки (соотношение прибыли к')
print('выручке). Далее запросите численность сотрудников фирмы и определите')
print('прибыль фирмы в расчете на одного сотрудника.\n')


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


def draw_chart(val, max_val, label):
    print(
        get_with_padding(label, ' ', 10),
        get_with_padding('', "#", int((val / max_val) * 20) or 1),
        ' ',
        f'${val: 0.2f}'
    )


done = False

any_key()
while not done:
    earnings = request_int('Input earnings >>> ')
    outgoings = request_int('Input outgoings >>> ')
    number_of_managers = request_int('Input number of managers >>> ')
    profit = earnings - outgoings

    print('\n')
    draw_chart(earnings, max(earnings, outgoings), 'EARNINGS:')
    draw_chart(outgoings, max(earnings, outgoings), 'OUTGOINGS:')

    if profit < 0:
        print(f'\nYou should fire your managers, your PROFIT (${profit: 0.2f}) is less then zero.')

    elif profit == 0:
        print(f'\nWell, at least we are still alive...')

    else:
        print(f'\nCongratulations!! We have PROFIT (${profit:0.2f})')
        print(f'Every of your {number_of_managers} managers will get BONUS equal ${(profit / number_of_managers):0.2f}')
        print(f'(Fire them all, they could work better)')

    if request_bool('\nDo you want to repeat? >>> '):
        done = False
    else:
        done = True
