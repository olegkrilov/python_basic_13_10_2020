from bycicles.input_requests import (
    request_boolean
)

from bycicles.helpers import (
    clear_screen,
    get_file_path,
    print_link_to_file
)

TARGET_FILE = 'task_1.txt'
BREAK_KEY = ''


def show_task():
    print('\nTASK # 1')
    print('Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.')
    print('Об окончании ввода данных свидетельствует пустая строка.\n')


def user_input(_str=''):
    clear_screen()
    show_task()

    if _str:
        print(_str)

    __str = input(' >>> ')
    _str += (__str + '\n')

    if __str == BREAK_KEY:
        clear_screen()
        show_task()
        print(_str)
        return _str

    else:
        return user_input(_str)


def main():
    done = False

    show_task()
    while not done:
        with open(f'files/{TARGET_FILE}', 'w', encoding='utf-8') as file:
            file.write(user_input())
            file.close()

        with open(f'files/{TARGET_FILE}', 'r', encoding='utf-8') as file:
            print(f'\nHere is the link to the file: {TARGET_FILE}')
            print_link_to_file(file)
            file.close()

        done = not request_boolean('\nRepeat ?')


if __name__ == '__main__':
    main()

