from homeworks.les_1.utils import any_key, request_int, request_bool, get_with_padding

print('3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.')
print('Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.\n')

done = False

while not done:
    any_key()
    user_number = request_int('Give me your number >>> ')
    equation_str = ''
    equation_total = 0
    i = 1
    lim = 3

    while i <= lim:
        value_str = str(user_number)
        arg = value_str * i
        equation_total += int(arg)
        i += 1
        equation_str += arg

        if i <= lim:
            equation_str += ' + '

    print(equation_str, equation_total, sep=' = ')

    if request_bool('Do you want to repeat? >>> '):
        done = False
    else:
        done = True
