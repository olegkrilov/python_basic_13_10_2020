from .helpers import (
    as_function
)


def _abstract_request(msg):
    return input(f'{msg} >>> ')


def request_from_list(
    list_of_values,
    msg=lambda _list: f'Select from "{_list}"',
    err_msg=lambda _str: f'ERROR: Unknown key "{_str}" '
):
    _user_choice = _abstract_request(as_function(msg, list_of_values)).lower()
    while _user_choice not in list_of_values:
        print(as_function(err_msg, _user_choice))
        return request_from_list(list_of_values, msg, err_msg)
    else:
        return _user_choice


def request_boolean(
    msg='',
    err_msg='Should select from [ Y / N ]'
):
    return request_from_list(
        ['y', 'n'],
        lambda _str: msg if callable(msg) else f'{msg} [ Y / N ]',
        as_function(err_msg)
    ) == 'y'


def request_number(
    msg='',
    err_msg='ERROR: Should be a number',
    get_float=False
):
    try:
        val = _abstract_request(msg)
        return float(val) if get_float else int(val)
    except ValueError:
        print(err_msg)
        return request_number(msg, err_msg)
