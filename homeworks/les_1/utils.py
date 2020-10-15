def any_key(custom_str='start'):
    input(f'press any key to {custom_str}\n')


def request_int(message='', error_message='Should be a number!'):

    try:
        return int(input(message))

    except ValueError as err:
        print(error_message or err)
        return request_int(message)


def request_bool(message='', error_message='Should be Y or N\n'):
    user_input = input(message).lower()

    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print(error_message)
        return request_bool(message, error_message)


def request_greater_int(threshold=0, message='', error_message='Should be a number!'):
    numb = request_int(message, error_message)

    if numb < threshold:
        print(f'Value should be greater then {threshold}')
        return request_greater_int(threshold, message, error_message)
    else:
        return numb


def get_with_padding(val, padding_symbol='0'):
    return str(val).rjust(2, padding_symbol)

