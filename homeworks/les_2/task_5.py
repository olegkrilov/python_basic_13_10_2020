import random

print('\n5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор')
print('натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.')
print('Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент')
print('с тем же значением должен разместиться после них.\n')


def request_to_continue():
    user_decision = str(input('Do you want to repeat (y / n) ? >>> ')).lower()
    if user_decision == 'y':
        return False
    elif user_decision == 'n':
        return True
    else:
        print('Type \'y\' or \'n\'')
        return request_to_continue()


def add_value():
    try:
        user_input = int(input('Type some INTEGER to add to the DATA >>> '))
        data.append(user_input)
        data.sort(reverse=True)
        return data

    except ValueError as err:
        print('Should be an INTEGER!')
        return add_value()


def generate_initial_data():
    initial_data = []
    data_size = random.randint(5, 10)
    while data_size:
        initial_data.append(random.randint(1, 999))
        data_size -= 1

    initial_data.sort(reverse=True)

    return initial_data


data = generate_initial_data()
print(f'Initial data:\n{data}')

done = False
while not done:

    add_value()
    print(f'\nUpdated data:\n{data}\n')

    done = request_to_continue()
