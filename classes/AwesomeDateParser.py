import re
from calendar import (
    month_name,
    monthrange
)


class FormatException(Exception):
    def __init__(self, err_message='ERROR: Bad format'):
        self.txt = err_message


class AwesomeDateParser:

    __required_format = '^[\d]{1,2}-[\d]{1,2}-[\d]{1,4}$'

    def __init__(self, date_str = None):
        self.__data = date_str

    def __str__(self):
        _date = self.date

        if _date is None:
            return f'Current value [{self.__data}] is unacceptable'

        else:
            return f'{_date["month"]}, {_date["day"]} of {_date["year"]}'

    def __call__(self):
        print(self)

    @property
    def date(self):
        return AwesomeDateParser.parse_date_string(self.__data)

    @property
    def required_format(self):
        return AwesomeDateParser.__required_format

    @date.setter
    def date(self, value=None):
        try:
            self.__data = str(value)
        except ValueError:
            print('Should be a string')

    @classmethod
    def parse_date_string(cls, date_str):
        try:
            if re.match(cls.__required_format, date_str) is None:
                raise FormatException()

            _day, _month, _year = [int(_val) for _val in date_str.split('-')]

            if AwesomeDateParser.validate_date_attributes(_day, _month, _year):
                return {
                    'day': str(_day),
                    'month': month_name[_month],
                    'year': str(_year)
                }
            else:
                raise FormatException()

        except ValueError:
            raise FormatException

        except FormatException:
            return None

    @staticmethod
    def validate_date_attributes(*args):
        try:
            _day, _month, _year = args

            return all(checker() for checker in [
                lambda: all(args) > 0,
                lambda: 1 <= _month <= 12,
                lambda: 1 <= _day <= monthrange(_year, _month)[1]
            ])

        except ValueError:
            return False


if __name__ == '__main__':
    valid_date = AwesomeDateParser('13-05-1984')
    invalid_date = AwesomeDateParser('19-45-12312')

    print(valid_date)
    valid_date()
    invalid_date()

