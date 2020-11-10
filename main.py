from controllers.Task1 import Task1
from controllers.Task2 import Task2
from controllers.Task3 import Task3
from controllers.Task4 import Task4
from controllers.Task7 import Task7

from common.utils import (
    clear_screen,
    request_from_list
)


def select_task():

    tasks = {
        '1': (lambda: Task1(), 'Task#1'),
        '2': (lambda: Task2(), 'Task#2'),
        '3': (lambda: Task3(), 'Task#3'),
        '4': (lambda: Task4(), 'Task#4'),
        '7': (lambda: Task7(), 'Task#7'),
        'q': (lambda: None, 'Quit'),
    }

    print('Select Task or [Q] to quit:')
    print('-' * 40)
    for key, val in tasks.items():
        print(f'[{key.upper()}]:', f'{val[1]}')

    return tasks[request_from_list([key for key in tasks.keys()], '\n')][0]()


def main():
    is_done = False

    while not is_done:
        clear_screen()
        task = select_task()

        if task is None:
            is_done = True
        else:
            task()


if __name__ == '__main__':
    main()




