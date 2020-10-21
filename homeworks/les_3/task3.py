from functools import reduce

print('\n3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,')
print('и возвращает сумму наибольших двух аргументов.\n')


def request_bool(message=''):
    choice = str(input(f'{message} (y / n)? >>> ')).lower()
    if choice in ['y', 'n']:
        return choice == 'y'
    else:
        print('Type Y or N')
        return request_bool(message)


def request_number(message=''):
    try:
        return float(input(message + ' >>> '))
    except ValueError:
        print('ValueError: Should be a NUMBER')
        return request_number(message)


def my_func(*args):
    return (
        f'{args[0]} + {args[1]}',
        reduce(lambda agg, val: agg + val, args[0: 2])
    )


def main():
    done = False

    while not done:
        args = tuple(
            sorted(
                [request_number('Input some number') for i in range(3)],
                reverse=True
            )
        )
        resp = my_func(*args)

        print(f'\n{resp[0]} = {resp[1]}')

        done = not request_bool('\nWould you like to repeat')


main()
