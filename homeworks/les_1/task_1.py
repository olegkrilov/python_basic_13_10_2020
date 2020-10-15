import random
import string
from homeworks.les_1.utils import any_key, request_int, request_greater_int

print('1. Поработайте с переменными, создайте несколько, выведите на экран,')
print('запросите у пользователя несколько чисел и строк и')
print('сохраните в переменные, выведите на экран.\n')

"""
STRINGS
"""

any_key()
some_string_variable = ''
number_of_words = random.randint(3, 7)
uppercase_chars = string.ascii_uppercase
lowercase_chars = string.ascii_lowercase

print(f'Generating random string with {number_of_words} words >>>')

while number_of_words > 0:
    number_of_words -= 1
    word_length = random.randint(5, 10)
    some_string_variable += random.choice(uppercase_chars)

    while word_length > 1:
        word_length -= 1
        some_string_variable += random.choice(lowercase_chars)

    if number_of_words:
        some_string_variable += ' '
    else:
        some_string_variable += '!'

print(some_string_variable, "\n")
print('Wow, we almost called Khtulhu...')
print('We should be more careful\n\n')


"""
NUMBERS & INTERACTIVITY
"""
any_key('continue')
print('\n\nNow let\'s add some interactivity')
print('Program will generate 10 numbers in user selected range\n\n')
number_of_steps = 10
numbers_range = [0, 0]

numbers_range[0] = request_int('Input FROM value >>> ')
numbers_range[1] = request_greater_int(numbers_range[0], f'Input TO value (greater then {numbers_range[0]}) >>> ')
# try:
#     custom_min_val += int(input('Input FROM value >>>'))
#     # numbers_range[0] += custom_min_val
#
# except ValueError as err:
#     print('Should be a number!')

#
# while not numbers_range[1]:
#     try:
#         custom_max_val = int(input(f'Input TO value (should be greater then {numbers_range[0]})>>>'))
#
#         if custom_max_val < numbers_range[0]:
#             print(f'Should be greater then {numbers_range[0]}')
#
#         else:
#             numbers_range[1] += custom_max_val
#
#     except ValueError as err:
#         print('Should be a number!')


min_val = 0
max_val = 0
total_val = 0
average_int = 0

number_of_steps_left = number_of_steps

while number_of_steps_left:
    number_of_steps_left -= 1
    val = random.randint(numbers_range[0], numbers_range[1])
    total_val += val

    if not min_val or min_val > val:
        min_val = val

    if not max_val or max_val < val:
        max_val = val

print(f'\n\nAfter generating {number_of_steps} random integers\nin range from {numbers_range[0]} to {numbers_range[1]}:\n\n')
print(f'MIN IS: {min_val}')
print(f'MAX IS: {max_val}')
print(f'AVERAGE (INT): {int(total_val / number_of_steps)}\n')
