from importlib import import_module

from bycicles.input_requests import (
    request_boolean,
    request_from_list
)

BREAK_KEY = 'q'


def select_task(tasks_list, break_key=BREAK_KEY):
    done = False

    while not done:

        list_of_keys = [break_key]
        msg = f'\nSelect task:\n' + ('-' * 42) + '\n'

        for index, key in enumerate(tasks_list):
            list_of_keys.append(f'{index + 1}')
            msg += f'[{index + 1}]: for {key}\n'

        msg += '[Q]: to quit \n'

        user_choice = request_from_list(
            list_of_keys,
            msg
        )

        if user_choice == break_key:
            done = True
        else:
            try:
                tasks_list[f'task_{user_choice}'].main()
            except KeyError as err:
                print(err)


def main():
    done = False
    tasks_list = {}

    for task in [f'task_{_i + 1}' for _i in range(7)]:
        tasks_list[task] = import_module(f'tasks.{task}')

    while not done:
        select_task(tasks_list)
        done = not request_boolean('Do you want to continue ? ')
    else:
        print('Bye!')


if __name__ == '__main__':
    main()
