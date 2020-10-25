# from time import sleep
# from my_module import (
#     func_a,
#     func_b
# )
# import datetime as dt
# from itertools import cycle


def tricky_sorter(items):
    return sorted(
        sorted(items), key=lambda _val: items.count(_val), reverse=True
    )


some_list = [3, 4, 11, 13, 11, 4, 4, 7, 3]


print(tricky_sorter(some_list))



# from collections import defaultdict
#
#
# def anagram_reader(list_of_words: list):
#     result = []
#     pre_result = {}
#
#     for _str in list_of_words:
#         try:
#             pre_result[''.join(sorted(_str))].append(_str)
#         except KeyError:
#             pre_result[''.join(sorted(_str))] = [_str]
#
#     return list(pre_result.values())
#
#
# test = defaultdict(str)(['hello', 'dear', 'gb', 'olelh', 'arde'])
#
# print(anagram_reader(test))


# print(func_b())
# print(func_a())
#
# print(dt.datetime.now().timestamp())
#
# some_date = '1984-20-12 15:22'
# print(dt.datetime.strptime(some_date, '%Y-%d-%m %H:%M'))




#
# some_list = ['a', 'b', 'c', 'd']
#
#
# def custom_iterator(values, base_index=0, step=1):
#     _done = False
#     _index = base_index
#     while not _done:
#         try:
#             _index += step
#             yield next(values), _index - step
#         except IndexError:
#             _done = True
#
#
# print(
#     custom_iterator(some_list)
# )
#
# for val, index in custom_iterator(some_list):
#     print(val, index)
