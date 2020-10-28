from bycicles.input_requests import (
    request_boolean
)

from bycicles.helpers import (
    clear_screen,
    get_file_path
)

TARGET_FILE = 'task_2.txt'
SPACE_KEY = ' '


def show_task():
    print('\nTASK # 2')
    print('Создать текстовый файл (не программно), сохранить в нем несколько строк,')
    print('выполнить подсчет количества строк, количества слов в каждой строке.\n')


def main():
    done = False

    while not done:
        clear_screen()
        show_task()

        with open(f'files/{TARGET_FILE}', 'r', encoding='utf-8') as file:
            for ind, __str in enumerate([_str.strip() for _str in file.read().split(sep='\n') if len(_str)]):
                print(f'\n{ind}: \n', __str, '\n', ('-' * 80))
                print('String size: ', len(__str))
                print('Count of words: ', len(__str.split(SPACE_KEY)))

            file.close()

        done = not request_boolean('\nRepeat ?')


if __name__ == '__main__':
    main()
