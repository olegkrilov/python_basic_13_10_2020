print('2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы')
print(' с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.')
print('Для заполнения списка элементов необходимо использовать функцию input().\n')

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


def request_int(msg='Input some number >>> '):
    try:
        return int(input(msg))
    except ValueError as err:
        print('Should be an INTEGER')
        return request_int(msg)


while not done:
    print('\nLet suppose we have some EMPTY LIST.')
    print('And you may fill it with some data.\n')

    initial_list = []
    result_list = []
    number_of_items = request_int('Input list size (INTEGER) >>> ')
    i = 0

    while i < number_of_items:
        i += 1
        initial_list.append(input(f'Item # {i} (ANY TYPE): >>> '))

    print('Ok. Now let\'s do some magic!')

    evens = initial_list[0::2]
    odds = initial_list[1::2]

    for ii in range(len(evens)):
        if ii < len(odds):
            print(evens[ii], '<==>', odds[ii])
            result_list.append(odds[ii])
        else:
            print(evens[ii], '<==>', evens[ii])

        result_list.append(evens[ii])

    print('REARRANGE RESULT IS: ', result_list)

    done = request_to_continue()
