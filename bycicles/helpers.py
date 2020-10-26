from time import (
    sleep
)


def as_function (obj, *args):
    return obj(*args) if callable(obj) else obj


def show_data(data, label):
    length = len(data)
    last_index = length - 1
    msg = '['
    print(f'\n{label}\n' + ('-' * 80))

    for index, val in enumerate(data):
        msg += str(val) + (', ' if index < last_index else '')
        print(str(msg).ljust(80, ' '), end='\r')
        sleep(.1)

    print(msg, ']', end='\n')
