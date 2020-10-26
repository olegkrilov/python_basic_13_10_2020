from functools import reduce

from bycicles.input_requests import (
    request_boolean
)


def show_task():
    print('\nTASK # 5')
    print('Реализовать формирование списка, используя функцию range() и возможности генератора.')
    print('В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат')
    print('вычисления произведения всех элементов списка.\n')


def main():
    done = False

    show_task()
    while not done:
        data = [val for val in range(100, 1001) if not val & 1]
        print(data)

        if request_boolean('\nDo you want to see some magic? '):
            print('\n', reduce(lambda val, agg: val * agg, data), '\nIsn\'t it really BIIIIG?')

        done = not request_boolean('\nRepeat')


if __name__ == '__main__':
    main()
