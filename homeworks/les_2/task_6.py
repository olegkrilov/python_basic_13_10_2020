import string

print('\n6. * Реализовать структуру данных «Товары». Она должна представлять собой')
print('список кортежей. Каждый кортеж хранит информацию об отдельном товаре.')
print('В кортеже должно быть два элемента — номер товара и словарь с параметрами')
print('(характеристиками товара: название, цена, количество, единица измерения).')
print('Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.\n')

database = []


def generate_datum():
    datum = {}


def select_from(items, message='Select from ', error_message='ERROR: Unknown command!\n'):
    item = str(input(message)).lower()

    if item in items:
        return item
    else:
        print(error_message)
        return select_from(items, message, error_message)


def get_int(message='Input value (INT) >>> ', min_val=0, max_val=0):
    try:
        val = int(input(message))

        if val < min_val:
            print(f'ERROR: Value should be bigger then {min_val}')
            return get_int(message,min_val,max_val)
        elif max_val and (max_val < val):
            print(f'ERROR: Value should be less then {max_val}')
            return get_int(message, min_val, max_val)
        else:
            return val

    except ValueError as err:
        print('ERROR: Should be an integer!')
        return get_int(message, min_val, max_val)


def add_product():
    existing_products = {}
    product = {}

    print('\nCREATE PRODUCT\n')

    for item in database:
        existing_products[item[1]['name']] = item[0]

    while 'name' not in product:
        some_name = input('Product name >>> ')

        if some_name in existing_products:
            print('ERROR: Product is already exist')
        else:
            product['name'] = some_name

    while 'unit' not in product:
        some_unit_name = input('Unit >>> ')
        product['unit'] = some_unit_name if len(some_unit_name) else 'items'

    product['price'] = get_int(f'Input price for 1 [{product["name"]}] >>> ')
    product['quantity'] = get_int(f'Input current quantity of [{product["name"]}] >>> ')

    database.append((str(len(database) + 1), product))

    print(f'\nProduct [{product["name"]}] was added successfully!\n')


def change_quantity():
    products = {}
    product_codes = []
    message = ''

    print('\nUPDATE PRODUCT\n')

    for item in database:
        product_codes.append(item[0])
        products[item[0]] = item[1]
        message += f'\n{item[0]}: {item[1]["name"]}'

    product = products[select_from(
        product_codes,
        f'Select product: {message} \n >>> '
    )]
    action = select_from(
        ['+', '-'],
        f'Press (+) to add or (-) to subtract [{product["name"]}] >>> '
    )
    delta = get_int(f'Input number of [{product["unit"]}] to {"add" if action == "+" else "subtract"} >>> ')

    if action == '+':
        product['quantity'] += delta
    elif action == '-':
        _val = product['quantity'] - delta
        product['quantity'] = _val if _val >= 0 else 0

    print(f'\nProduct [{product["name"]}] was updated successfully!\n')


def get_statistics():
    columns = {
        'Code': {
            'size': 0,
            'values': []
        },
        'Name': {
            'size': 0,
            'values': []
        },
        'Price': {
            'size': 0,
            'values': []
        },
        'Qty': {
            'size': 0,
            'values': []
        },
        'Total': {
            'size': 0,
            'values': []
        }
    }

    print('\nCURRENT STATISTICS:\n')

    for item in database:
        code = str(item[0])
        name = item[1]['name']
        price = str(item[1]['price'])
        qty = str(item[1]['quantity'])
        total = str(item[1]['price'] * item[1]['quantity'])

        columns['Code']['size'] = max([len('Code'), columns['Code']['size'], len(code)])
        columns['Name']['size'] = max([len('Name'), columns['Name']['size'], len(name)])
        columns['Price']['size'] = max([len('Price'), columns['Price']['size'], len(price)])
        columns['Qty']['size'] = max([len('Qty'), columns['Qty']['size'], len(qty)])
        columns['Total']['size'] = max([len('Total'), columns['Total']['size'], len(total)])

        columns['Code']['values'].append(code)
        columns['Name']['values'].append(name)
        columns['Price']['values'].append(price)
        columns['Qty']['values'].append(qty)
        columns['Total']['values'].append(total)

    grid_header = ''
    row_index = 0

    for key in columns:
        column = columns[key]
        grid_header += str(key).rjust(column['size'] + 5)

    print(grid_header)

    for row in database:
        grid_row = ''

        for key in columns:
            column = columns[key]
            grid_row += column['values'][row_index].rjust(column['size'] + 5)

        row_index += 1
        print(grid_row)

    print('\n\n')


def get_required_action():
    required_action = select_from(
        ['p', 'c', 's', 'q'],
        'Select task:\n\tP: Add product\n\tC: Change quantity \n\tS: Get statistics \n\tQ: Quit\n\t>>> '
    )

    if required_action == 'p':
        return add_product
    elif required_action == 'c':
        return change_quantity
    elif required_action == 's':
        return get_statistics
    elif required_action == 'q':
        return None
    else:
        print('ERROR: Unknown command!\n')
        return get_required_action()


def main():
    done = False

    while not done:
        action = get_required_action()

        if action:
            action()
        else:
            done = True


main()

