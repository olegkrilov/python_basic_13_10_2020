import random
import string

print('1. Поработайте с переменными, создайте несколько, выведите на экран,')
print('запросите у пользователя несколько чисел и строк и')
print('сохраните в переменные, выведите на экран.\n')


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


def get_with_padding(some_val, padding_symbol='0', length=2):
    return str(some_val).rjust(length, padding_symbol)


""""
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
