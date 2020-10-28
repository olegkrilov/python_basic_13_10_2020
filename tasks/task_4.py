import re

from googletrans import (
    Translator
)

from bycicles.input_requests import (
    request_boolean
)

from bycicles.helpers import (
    clear_screen,
    print_link_to_file
)

SOURCE_FILE = 'task_4_en.txt'
TARGET_FILE = 'task_4_ru.txt'
SPACE_KEY = ' '
NEW_LINE_KEY = '\n'


def show_task():
    print('\nTASK # 1')
    print('Создать (не программно) текстовый файл со следующим содержимым:\nOne — 1\nTwo — 2\nThree — 3\nFour — 4')
    print('Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.')
    print('При этом английские числительные должны заменяться на русские. Новый блок строк')
    print('должен записываться в новый текстовый файл.')


def main():
    done = False
    translate = Translator().translate

    while not done:
        data = []

        clear_screen()
        show_task()

        with open(f'files/{SOURCE_FILE}', 'r', encoding='utf-8') as file:
            data += [
                re.sub('^\w*', translate(_str.split(SPACE_KEY)[0], src='en', dest='ru').text, _str)
                for _str in file.read().split(NEW_LINE_KEY)
            ]

            print(f'\nOriginal File: {SOURCE_FILE}')
            print_link_to_file(file)

            file.close()

        with open(f'files/{TARGET_FILE}', 'w', encoding='utf-8') as file:
            content = ''
            for _str in data:
                content += (_str + NEW_LINE_KEY)

            file.write(content)

            print(f'\nTranslated File: {TARGET_FILE}')
            print_link_to_file(file)

            file.close()

        done = not request_boolean('\nRepeat ?')


if __name__ == '__main__':
    main()

