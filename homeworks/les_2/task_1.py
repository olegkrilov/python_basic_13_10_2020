import random
import string

print('1. Создать список и заполнить его элементами различных типов данных.')
print('Реализовать скрипт проверки типа данных каждого элемента. Использовать')
print('функцию type() для проверки типа. Элементы списка можно не запрашивать')
print('у пользователя, а указать явно, в программе.\n')


done = False


def request_to_continue():
    user_decision = str(input('Do you want to repeat (y / n) ? >>> ')).lower()
    if user_decision == 'y':
        return False
    elif user_decision == 'n':
        return True
    else:
        print('Type \'y\' or \'n\'')
        return request_to_continue()


def get_random_string(str_length=0):
    if not str_length:
        str_length = random.randint(3, 10)

    return ''.join(random.choice(string.ascii_letters) for _i in range(str_length))


def get_random_number():
    return random.randint(0, 999999)


def get_none():
    return None


def get_random_dictionary():
    return {
        'String': get_random_string(),
        'Number': get_random_number(),
        'None': get_none()
    }


def get_random_tuple():
    return get_random_string(), get_random_number()


while not done:
    some_list = []
    actions = {
        'String': get_random_string,
        'Number': get_random_number,
        'None': get_none,
        'Dictionary': get_random_dictionary,
        'Tuple': get_random_tuple
    }
    actions_keys = list(actions.keys())
    i = 10

    print('So, we have a List, and it is empty')
    print('let\'s fill it with some different and random data! ....\n')

    while i:
        i -= 1
        action_key = random.choice(actions_keys)

        some_list.append(actions[action_key]())

    print('Generated data is: ')
    for datum in some_list:
        i += 1
        datum_type = type(datum)

        if datum_type is dict:
            print(f'{i}) TYPE: {datum_type}')
            for key in datum:
                print(f'\tKEY: {key}, VALUE: {datum[key]}, TYPE: {type(datum[key])}')
            print('\n')

        elif datum_type is tuple:
            print(f'{i}) TYPE: {datum_type}')
            for sub_datum in datum:
                print(f'\tDATUM: {sub_datum}, TYPE: {type(sub_datum)}')
            print('\n')

        else:
            print(f'{i}) DATUM: {datum}, TYPE: {datum_type}\n')

    done = request_to_continue()
