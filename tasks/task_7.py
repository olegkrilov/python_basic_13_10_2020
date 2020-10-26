from itertools import (
    count
)
from bycicles.input_requests import (
    request_number,
    request_boolean
)


def show_task():
    print('\nTASK # 7')
    print('Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.')
    print('При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:')
    print('for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить')
    print('только первые n чисел, начиная с 1! и до n!.\n')


def get_fact_limit():
    limit = request_number('\nInput limit for Factorial Generator:')

    if limit <= 0:
        print('ERROR: Should be equal or bigger then 1\n')
        return get_fact_limit()
    else:
        return limit


def fact(n):
    _agg = 1
    _i = 1
    while _i <= n:
        yield _agg
        _agg *= _i
        _i += 1


def main():
    done = False

    while not done:
        n = get_fact_limit()
        generator = fact(n + 1)

        for val in range(n + 1):
            print(f'!{val} = {next(generator)}')

        done = not request_boolean('\nRepeat')


if __name__ == '__main__':
    main()
