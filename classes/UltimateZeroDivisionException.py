from time import sleep


class UltimateZeroDivisionException(Exception):

    def __init__(self, message=f'Uni\u2555\u2593rse wa\u255c coll\u2554psed succ\u2566sfullllllllllllyyyyyyy...\n'):
        self.message = message

    def __str__(self):

        print('\nWARNING! Attempt to divide by zero!')
        print('Universe collapsing protocol activated')
        _i = 0
        while _i <= 100:
            print(('\u2593' * _i) + f' {_i}%' + (' ' * (100 - _i)), end='\r')
            _i += 1
            sleep(.1)
        else:
            print('\n\n')

        return self.message


if __name__ == '__main__':
    val_a = 10000
    val_b = 0

    try:
        print(val_a / val_b)

    except ZeroDivisionError:
        try:
            raise UltimateZeroDivisionException()
        except UltimateZeroDivisionException as err:
            print(err)
