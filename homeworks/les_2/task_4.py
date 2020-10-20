import string
import random

print('\n4. Пользователь вводит строку из нескольких слов, разделённых пробелами.')
print('Вывести каждое слово с новой строки. Строки необходимо пронумеровать.')
print('Если в слово длинное, выводить только первые 10 букв в слове.\n')


def request_to_continue():
    user_decision = str(input('Do you want to repeat (y / n) ? >>> ')).lower()
    if user_decision == 'y':
        return False
    elif user_decision == 'n':
        return True
    else:
        print('Type \'y\' or \'n\'')
        return request_to_continue()


def get_random_string (str_len=0):
    random_string = ''

    if not str_len:
        str_len = random.randint(3, 10)

    while str_len:
        str_len -= 1
        substr_len = random.randint(7, 15)
        random_string += ''.join(random.choice(string.ascii_letters) for _i in range(substr_len))

        if str_len:
            random_string += ' '

    return random_string


def get_initial_string():
    input_method = str(input('Would you like to generate random phrase? (y, n) >>> ')).lower()

    if input_method == 'y':
        return get_random_string()

    elif input_method == 'n':
        return input('Type few words >>> ')

    else:
        print('Please, type (y or n)')
        return get_initial_string()


def get_sharded_string(some_string):
    sharded_string = some_string.split(sep=' ')

    return sharded_string


done = False
while not done:
    initial_string = get_initial_string()
    i = 1

    print(f'\n{initial_string} => ')

    for word in get_sharded_string(initial_string):
        print(f'{i}: {word[0: 10]}{"..." if len(word) > 10 else ""}')
        i += 1

    done = request_to_continue()
