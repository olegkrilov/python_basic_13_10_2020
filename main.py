from common.utils import (
    request_from_list,
    clear_screen
)
from tasks.TaskOne.TaskOne import TaskOne
from tasks.TaskTwo.TaskTwo import TaskTwo
from tasks.TaskThree.TaskThree import TaskThree
from tasks.TaskFour.TaskFour import TaskFour


def select_task():
    tasks = {
        '1': TaskOne,
        '2': TaskTwo,
        '3': TaskThree,
        '4': TaskFour,
        'q': None
    }

    print('Select Task or [Q] to quit:')
    print('-' * 40)
    for key, val in tasks.items():
        print(f'[{key.upper()}]:', f'Task#{key}' if val else 'Quit')

    return tasks[request_from_list([key for key in tasks.keys()], ' ')]


def main():
    done = False

    while not done:
        clear_screen()
        task = select_task()

        if task is None:
            done = True
        else:
            task().init()


if __name__ == '__main__':
    main()
