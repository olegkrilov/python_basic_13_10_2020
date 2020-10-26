from bycicles.input_requests import (
    request_boolean
)
from bycicles.helpers import (
    show_data,
    generate_seed
)


def show_task():
    print('\nTASK # 4')
    print('Представлен список чисел. Определить элементы списка, не имеющие повторений.')
    print('Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования')
    print('в исходном списке. Для выполнения задания обязательно использовать генератор.\n')


def main():
    done = False

    while not done:
        data = generate_seed(1, 9)
        unique_values = [val for val in {key: True for key in data}.keys()]

        show_data(data, 'Original Data')
        show_data(unique_values, 'Unique Values')

        done = not request_boolean('\nRepeat')


if __name__ == '__main__':
    main()
