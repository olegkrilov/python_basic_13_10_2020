from homeworks.les_1.utils import any_key, request_int, request_bool

print('4. Пользователь вводит целое положительное число. Найдите самую')
print('большую цифру в числе. Для решения используйте цикл while и')
print('арифметические операции.')

done = False

any_key()

while not done:

    user_input = str(request_int('Give me a number - BIG number, please >>> '))
    max_val = 0
    i = 0
    str_len = len(user_input)

    while i < str_len:
        max_val = max(int(user_input[i]), max_val)
        i += 1

    print(f'\n\nMax value in {user_input} is {max_val}')

    if request_bool('\nDo you want to repeat? >>> '):
        done = False
    else:
        done = True
