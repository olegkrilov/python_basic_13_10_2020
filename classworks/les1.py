# todo: google PEP-8

print('hello world')

# some_var = 1
# some_another_var = '1'  # two spaces after the code
# some_decimal = 22.343453
#
# print(type(some_var))
# print(type(some_another_var))
# print('asd' * 3)


name = input('Name? \n>>>')
surname = input('Surname? \n>>>')
age = int(input('Age?\n>>>'))
threshold_age = 18


if age >= threshold_age:
    print(f'{name:>25}\n{surname:<25}\nwas born in\n{2020 - age:^25}')
else:
    print(f'Go away, {name} {surname}', end='!')

# todo: remember to use & instead of num_a % 2
