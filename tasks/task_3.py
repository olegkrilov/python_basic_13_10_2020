from bycicles.input_requests import (
    request_boolean
)


def show_task():
    print('\nTASK # 1')
    print('Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.')
    print('Об окончании ввода данных свидетельствует пустая строка.\n')


def main():
    done = False

    show_task()
    while not done:

        done = not request_boolean('Repeat ?')


if __name__ == '__main__':
    main()

