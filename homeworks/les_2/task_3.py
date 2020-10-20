from functools import reduce
import calendar

print('\n3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года')
print('относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.\n')


# Constants
DICT = 'dict'
LIST = 'list'
DATA = 'data'
DATA_TYPE = 'data_type'
GETTER = 'getter'


# Methods
def request_to_continue():
    user_decision = str(input('Do you want to repeat (y / n) ? >>> ')).lower()
    if user_decision == 'y':
        return False
    elif user_decision == 'n':
        return True
    else:
        print('Type \'y\' or \'n\'')
        return request_to_continue()


def request_month():
    try:
        user_decision = int(input('\nInput number of month [1 - 12] >>> '))

        if 1 <= user_decision <= 12:
            return user_decision
        else:
            print('Value should be between 1 and 12')
            return request_month()

    except ValueError as err:
        print('Value should be an integer between 1 and 12!')
        return request_month()


def get_from_list(data):

    def _get_from_list(index):
        return data[index - 1]

    return _get_from_list


def get_from_dict(data):

    def _get_from_dict(index):
        return data[calendar.month_name[index]]

    return _get_from_dict


def request_method():
    user_decision = str(input('Press (L) to use List, Press (D) to use Dictionary >>> ')).lower()

    if user_decision == 'l' or user_decision == 'd':
        data_getter = None
        data_type = ''
        data = None

        if user_decision == 'l':
            data = []
            data_type = LIST
            data_getter = get_from_list(data)

        elif user_decision == 'd':
            data = {}
            data_type = DICT
            data_getter = get_from_dict(data)

        for i in range(1, 13):
            season = ''
            month_name = calendar.month_name[i]

            if 1 <= i <= 2 or i == 12:
                season += 'Winter'
            elif 3 <= i <= 5:
                season += 'Spring'
            elif 6 <= i <= 8:
                season += 'Summer'
            elif 9 <= i <= 11:
                season += 'Autumn'

            item = (i, month_name, season)

            if data_type == LIST:
                data.append(item)
            elif data_type == DICT:
                data[month_name] = item

        print(f'So, the program will work with <{data_type}>')
        print('Data: ')
        print(data)

        return data_getter

    else:
        print('Select (L) or (D)')
        return request_method()


done = False
while not done:
    getter = request_method()
    datum = getter(request_month())

    print(f'\nYour month is {datum[1]} and it belongs to {datum[2]}\n')

    done = request_to_continue()
