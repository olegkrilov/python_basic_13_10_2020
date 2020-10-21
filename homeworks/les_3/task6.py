print('\n6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв')
print('и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.\n')
print('Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.')
print('Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое')
print('слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().\n')

SEPARATOR_SYMBOL = ' '


def request_bool(message=''):
    choice = str(input(f'{message} (y / n)? >>> ')).lower()
    if choice in ['y', 'n']:
        return choice == 'y'
    else:
        print('Type Y or N')
        return request_bool(message)


def int_func(some_string):
    return some_string[0].upper() + some_string[1:]
    # We can just use str.capitalize, but whatever...


def main():
    done = False

    while not done:
        [
            print(int_func(_str)) for _str
            in input(f'Input some text separated with "{SEPARATOR_SYMBOL}"\n >>> ').split(SEPARATOR_SYMBOL)
        ]

        done = not request_bool('Do you want to repeat')


main()
