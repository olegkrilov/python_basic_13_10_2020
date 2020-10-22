from inspect import signature
from random import randint

"""
map, zip, reduce, sorted, max, min, sum, range, round, divmod
"""

# Constants
EMPTY_STRING = ''
USE_RANDOM_AS_BASE = 'random'
USE_FIRST_AS_BASE = 'first'
USE_LAST_AS_BASE = 'last'


# Privates
def _iterator(action, items):
    _i = 0
    for item in items:
        _i += 1
        _val = action(item, _i - 1)
        yield _val


def _do_iteration(_iterable, _res=None):
    _done = False
    while not _done:
        try:
            next(_iterable)
        except StopIteration:
            _done = True

    return _res


def _is_iterable(some_obj):
    try:
        return bool(iter(some_obj))
    except TypeError:
        return False


# Exportable
def indexed_filter(checker, items, include_indexes=True):
    def _do_check(_checker, _val, _index, _res):
        if _checker(_val, _index):
            _res.append((_val, _index) if include_indexes else _val)

    _res = []

    return _do_iteration(
        _iterator(lambda _val, _index: _do_check(checker, _val, _index, _res), items),
        _res
    )


def indexed_map(action, items, *args):
    def _do_action(_action, _val, _index, _args, _res):
        _res.append(action(_val, _index, *_args) if _args else action(_val, _index))

    _args = args[0:len(signature(action).parameters.keys())] if len(args) else None
    _res = []

    return _do_iteration(
        _iterator(lambda _val, _index: _do_action(action, _val, _index, _args, _res), items),
        _res
    )


def indexed_zip(items, *args):
    def _do_append(_resp, _sequence, _index):
        try:
            _resp.append(_sequence[_index])
        except IndexError:
            _resp.append(None)

    def _do_zip(_item, _index, _sequences):
        _resp = [_index, _item]

        return tuple(
            _do_iteration(
                _iterator(
                    lambda _sequence, _: _do_append(_resp, _sequence, _index),
                    _sequences
                ),
                _resp
            )
        )

    return indexed_map(
        _do_zip,
        items,
        indexed_filter(lambda _obj, _index: _is_iterable(_obj), args, False)
    )


def custom_reduce(action, items, value=None):
    _no_initial_value = value is None
    _core = {}
    _items = items[1:] if _no_initial_value else items

    def _update_value(new_val):
        _core['value'] = new_val

    _update_value(items[0] if _no_initial_value else value)

    return _do_iteration(
        _iterator(lambda _val, _index: _update_value(action(_val, _index, _core['value'])), _items),
        lambda: _core['value']
    )()


def custom_sorted(items, reverse=False, use_base=USE_RANDOM_AS_BASE):

    def _put_val(_left_hand, _core, _right_hand, _base_val, _current_val):
        if _base_val > _current_val:
            _left_hand.append(_current_val)
        elif _base_val < _current_val:
            _right_hand.append(_current_val)
        else:
            _core.append(_current_val)

    _len = len(items)

    if _len < 2:
        return items

    else:
        _base_index = 0
        _lat_index = _len - 1
        _base = None
        _left_hand = []
        _core = []
        _right_hand = []

        if use_base == USE_RANDOM_AS_BASE:
            _base_index = randint(0, _lat_index)
        elif use_base == USE_LAST_AS_BASE:
            _base_index = _lat_index

        _base = items[_base_index]
        _core.append(_base)

        return _do_iteration(
            _iterator(
                lambda _val, _index: _index != _base_index and _put_val(
                    _left_hand,
                    _core,
                    _right_hand,
                    _base,
                    _val
                ),
                items
            ),
            lambda: custom_sorted(_left_hand) + _core + custom_sorted(_right_hand)
        )()[::-1 if reverse else 1]


def custom_min(items):
    return custom_sorted(items)[0]


def custom_max(items):
    return custom_sorted(items, True)[0]


def custom_sum(items):
    return custom_reduce(
        lambda _val, _, _sum: _sum + _val, items
    )


def custom_range(val, *args):
    _args_len = len(args)
    _start = val if _args_len >= 1 else 0
    _stop = val if _args_len < 1 else args[0]
    _step = args[1] if _args_len > 1 else 1
    _range = []

    def _update(_index):
        _range.append(_start + (_step * _index))

    return _do_iteration(
        _iterator(
            lambda _, _index: _update(_index),
            [None] * (((_stop - _start) // _step) + (1 if _step > 1 else 0))
        ),
        lambda: _range
    )()


def custom_divmod(numerator, denominator):
    if not denominator:
        denominator = 1

    return numerator // denominator, numerator % denominator


def custom_round(val, fraction=None):
    if fraction is None:
        fraction = 0

    _multiplier = 10 ** fraction
    _divmod = custom_divmod(val * _multiplier, 1)
    _float_str = str(_divmod[1])[2:]
    _float_sum = custom_reduce(
        lambda _str, _, _agg: _agg + int(_str),
        _float_str,
        0
    )
    _res = int(_divmod[0] + (1 if _float_sum / (len(_float_str) or 1) >= .5 else 0)) / _multiplier

    return _res if fraction else int(_res)


"""
TESTS TESTS TESTS
"""

"""
TEST ZIP
Response should be
(0, 'a', 0, 4, 'z') 0
(1, 'b', 1, 4, 'z') 1
(2, 'c', 2, 4, 'z') 2
(3, 'd', 3, None, None) 3
(4, 'e', 4, None, None) 4
(5, 'f', 5, None, None) 5
"""
print('\nTesting ZIP:')
_do_iteration(
    _iterator(
        print,
        indexed_zip(
            'abcdef',
            (0, 1, 2, 3, 4, 5, 10),
            [4, 4, 4],
            999,
            'zzz'
        )
    )
)


"""
TEST SORTED
Response should be
[-123123123, -2334, 0, 0.345345, 3, 12, 123123, 123123, 45634434235]
[45634434235, 123123, 123123, 12, 3, 0.345345, 0, -2334, -123123123]
"""
print('\nTesting SORTED:')
print(custom_sorted([123123, 123123, 45634434235, 12, 3, -2334, .345345, -123123123, 0]))
print(custom_sorted([123123, 123123, 45634434235, 12, 3, -2334, .345345, -123123123, 0], True))


"""
TEST REDUCE
Response should be
{0: ('zxc', 0), 1: ('asd', 1), 2: ('qwe', 2), 3: ('rty', 3), 4: ('vbn', 4)
"""


def test_reduce_fn(val, index, agg):
    agg[index] = (val, index)
    return agg


print('\nTesting REDUCE:')
print(
    custom_reduce(
        test_reduce_fn,
        ['zxc', 'asd', 'qwe', 'rty', 'vbn'],
        {}
    )
)


"""
TEST MIN & MAX
Response should be
MAX = 34523442431
MIN = -1233424
"""
some_values = [123123, 1232542345, 34523442431, 123123, -123, 1234453, 567567567, 0, -1233424, .5345345, 2123]
print('\nTesting MIN & MAX')
print(f'FROM {some_values}')
print(f'MAX = {custom_max(some_values)}\nMIN = {custom_min(some_values)}')


"""
TEST SUM
Response should be 
123332
qwe+zxc-vbn*
"""
print('\nTesting SUM')
some_another_values = [1, 2, 4, 135, 67, 123123]
some_strings = ('qwe+', 'zxc-', 'vbn*')
print(custom_sum(some_another_values))
print(custom_sum(some_strings))


"""
TEST RANGE
Response should be

11 33 55 77 99
11 12 13 14 15 16 17 18 19 20 21 22
0 1 2 3 4 5 6 7 8 9 10

"""
print('\nTesting RANGE')
print(*custom_range(11, 100, 22))
print(*custom_range(11, 23))
print(*custom_range(11))


"""
TEST ROUND
Response should be
123
124
123.895

"""
print('\nTesting ROUNDING (along with DIVMOD)')
print(custom_round(123))
print(custom_round(123.89434234234))
print(custom_round(123.89434234234, 3))
