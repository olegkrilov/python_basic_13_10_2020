print('\n5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.')
print('При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,')
print('разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться')
print('к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение')
print('программы завершается. Если специальный символ введен после нескольких чисел, то вначале')
print('нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.\n')

SEPARATOR_SYMBOL = ' '
STOP_SYMBOL = 'z'


def request_bool(message=''):
    choice = str(input(f'{message} (y / n)? >>> ')).lower()
    if choice in ['y', 'n']:
        return choice == 'y'
    else:
        print('Type Y or N')
        return request_bool(message)


def show_message(val):
    if val:
        print(f'Current sum = {val}')


def main():
    done = False
    total = 0

    while not done:
        for val in input(f'Print some numbers separated by "{SEPARATOR_SYMBOL}"\n >>> ').split(SEPARATOR_SYMBOL):
            if val.lower() == STOP_SYMBOL:
                break
            elif val.isdigit():
                total += float(val)
            else:
                pass

        if total:
            print(f'Current sum = {total}')

        done = not request_bool('\nWould you like to continue')


main()
