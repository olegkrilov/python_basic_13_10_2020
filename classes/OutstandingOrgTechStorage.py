from string import ascii_letters
from random import (
    choice,
    randint
)
from common.utils import as_list


SHOW_INQUIRIES = 'show inquiries'
SHOW_OFFERS = 'show offers'
SHOW_INFO = 'show info'
DEAL = 'deal'
BUY = 'buy'
SELL = 'sell'


def _get_uid(prefix='uid'):
    return f'{prefix}_' + ''.join([choice(ascii_letters) for _ in range(10)])


class ExtremelyReusableException(Exception):

    def __init__(self, message='Nooooooooo!'):
        self._message = message

    def __str__(self):
        return f'\nERROR: {self._message}\n'


class UnknownTechTypeException(ExtremelyReusableException):

    def __init__(self, message='Unknown type'):
        self._message = message


class NotEnoughItemsToCloseDeal(ExtremelyReusableException):

    def __init__(self, message='Insufficient amount'):
        self._message = message


class OutstandingOrgTechStorage:

    def __init__(self, money_own=1000000, max_capacity=1000, on_empty_message='Storage is Empty'):
        self.__categories = {}
        self.__money_own = float(money_own)
        self.__capacity = int(max_capacity)
        self.__on_empty_message = on_empty_message

    def __add__(self, deal):
        _category = deal['type']
        _items = as_list(deal['items'])
        _new_items = []
        _total_price = 0
        _total_size = 0
        _len = len(_items)
        _is_done = False
        _i = 0

        while _i < _len and not _is_done:
            _item = _items[_i]
            __total_price = _item.buy_price + _total_price
            __total_size = _item.size + _total_size

            if (__total_price > self.__money_own) or (__total_size > self.__capacity):
                _is_done = True

            else:
                if _category not in self.__categories:
                    self.__categories[_category] = []

                _new_items.append(_item)
                _total_price = __total_price
                _total_size = __total_size
                _i += 1

        if _len > len(_new_items):
            print('WARNING: can not accept the Cargo, not enough capacity and/or money.')

            return False

        else:
            self.__categories[_category] += _new_items
            self.__money_own -= _total_price
            self.__capacity -= _total_size

            return True

    def __sub__(self, deal):
        _category = deal['type']
        _qty = deal['quantity']

        try:
            _items = self.__categories[_category][0: _qty]

            try:
                if len(_items) < _qty:
                    raise NotEnoughItemsToCloseDeal(f'THere is no {_qty} of {_category}s in the Storage')
                else:
                    _total_profit = 0
                    _total_outgoing = 0

                    for _item in _items:
                        _total_profit += _item.sell_price
                        _total_outgoing += _item.size

                    self.__money_own += _total_profit
                    self.__capacity += _total_outgoing
                    del self.__categories[_category][0: _qty]

                    return True

            except NotEnoughItemsToCloseDeal as err:
                print(err)
                return False

        except KeyError:
            try:
                raise UnknownTechTypeException(f'OutstandingOrgTechStorage has no category named as {_category}.')
            except UnknownTechTypeException as err:
                print(err)
                return False

        # return self

    def __str__(self):

        _str = ''

        _str += 'Outstanding Org Tech Storage\n'
        _str += (('-' * 100) + '\n')
        _str += f'Current Liquidity: ${self.money_own}\n'
        _str += f'Current Capacity: {self.capacity}\n'
        _str += (('-' * 100) + '\n')

        if self.is_empty:
            _str += self.__on_empty_message

        else:
            for key, val in self.__categories.items():
                _str += f'{key.upper()}: {len(val)}\n'

        return _str

    @property
    def is_empty(self):
        return not any(len(_category) for _category in self.__categories.values())

    @property
    def money_own(self):
        return self.__money_own

    @property
    def capacity(self):
        return self.__capacity


class WonderfulOrgTechFactory:

    def __init__(self):
        self.__construction_lines = {
            'printer': OrdinaryOfficePrinter,
            'scanner': FlatAndNoisyScanner,
            'xerox': BigWhiteXerox
        }

    def create(self, tech_type, quantity):
        try:
            _line = self.__construction_lines[tech_type.lower()]
            return [_line() for _ in range(quantity)]

        except KeyError:
            try:
                raise UnknownTechTypeException(f'Factory is not able to produce technics of type "{tech_type}".')

            except UnknownTechTypeException as err:
                print(err)
                return []

    @property
    def available_types(self):
        return [key for key in self.__construction_lines.keys()]


class AmazingOrgTechMarket:

    __inquiry_index = 0
    __offer_index = 0

    def __init__(self):
        self.__factory = WonderfulOrgTechFactory()
        self.__inquiry = {}
        self.__offer = {}

        self.user_directives = {
            SHOW_INQUIRIES: (lambda: self.__show_inquiries(), 'see available INQUIRIES.', SHOW_INQUIRIES),
            SHOW_OFFERS: (lambda: self.__show_offers(), 'see available OFFERS', SHOW_OFFERS),
            SHOW_INFO: (lambda: self.__show_info(), 'read application INSTRUCTIONS', SHOW_INFO),
            DEAL: (lambda: None, 'buy or sell something', f'{DEAL} <deal uid>')
        }

        self.__refresh()

    def __str__(self):
        return self.__show_inquiries() + '\n' + self.__show_offers()

    def __call__(self, user_directive):
        try:
            _directive = user_directive.lower().strip()

            if _directive in self.user_directives:
                return self.user_directives[_directive][0]()

            if _directive.find(DEAL) >= 0:
                _, uid = _directive.split(' ')
                _uid = uid.upper()

                if _uid in self.__inquiry:
                    return self.__inquiry[_uid]

                elif _uid in self.__offer:
                    return self.__offer[_uid]

                else:
                    print(f'Sorry, can\'t find the DEAL with the requested uid: {_uid}')
                    return None

            else:
                raise KeyError()

        except KeyError:
            print('Sorry, can\'t understand your directive, could you please rephrase? ')
            return None
            # self()

    def __create_inquiries(self):
        _limit_of_inquiries = 5
        _delta = _limit_of_inquiries - len(self.__inquiry.keys())
        _i = 0

        while _i < _delta:
            _uid = f'INQ_{AmazingOrgTechMarket.__inquiry_index}'
            self.__inquiry[_uid] = {
                'uid': _uid,
                'deal': BUY,
                'quantity': randint(1, 99),
                'type': choice(self.__factory.available_types)
            }
            AmazingOrgTechMarket.__inquiry_index += 1
            _i += 1

        return self

    def __create_offers(self):
        _limit_of_offers = 5
        _delta = _limit_of_offers - len(self.__offer.keys())
        _i = 0

        while _i < _delta:
            _uid = f'OFF_{AmazingOrgTechMarket.__offer_index}'
            _type = choice(self.__factory.available_types)
            _quantity = randint(1, 99)

            self.__offer[_uid] = {
                'uid': _uid,
                'type': _type,
                'deal': SELL,
                'quantity': _quantity,
                'items': self.__factory.create(_type, _quantity)
            }
            AmazingOrgTechMarket.__offer_index += 1
            _i += 1

        return self

    def __show_inquiries(self):
        _str = '\nCURRENT INQUIRIES:\n'
        _str += ('-' * 100)
        for key, value in self.__inquiry.items():
            _str += f'\nWant to BUY {value["quantity"]} {value["type"]}s, {key}'

        return _str

    def __show_offers(self):
        _str = '\nCURRENT OFFERS:\n'
        _str += ('-' * 100)
        for key, value in self.__offer.items():
            _str += f'\nWant to SELL {value["quantity"]} {value["type"]}s, {key}'

        return _str

    def __show_info(self):
        _str = '\nINSTRUCTIONS:\n'
        _str += ('-' * 100)
        for key, val in self.user_directives.items():
            _str += f'\n[{val[2].capitalize()}] to {val[1]}'

        return _str

    def __refresh(self):
        self.__create_inquiries().__create_offers()
        return self

    def close_deal(self, deal):
        try:
            if deal['deal'] == SELL:
                del self.__offer[deal['uid']]

            elif deal['deal'] == BUY:
                del self.__inquiry[deal['uid']]

            self.__refresh()

        except KeyError:
            print(f'Sorry, deal with uid {deal["uid"]} is not registered.')


class OrgTechUnit:

    __nominal_price = 100

    def __init__(self, name='Nameless Org Tech', price=0, size=0):
        self.__name = name
        self.__price = price or OrgTechUnit.__nominal_price
        self.__size = size
        self.__uid = _get_uid(f'{self.__name}')

    def __str__(self):
        return f'TYPE: {self.name}\nPRICE: {self.sell_price}\nSIZE: {self.size}'

    def __call__(self):
        print(f'It is {self.name}')

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    @property
    def sell_price(self):
        return self.__price * 1.08

    @property
    def buy_price(self):
        return self.__price

    @property
    def size(self):
        return self.__size


class OrdinaryOfficePrinter(OrgTechUnit):

    def __init__(self, price=300):
        super().__init__(name='Printer', price=price, size=2)

    def __call__(self):
        print(f'{self.name} can print (what a surprise!!!)')


class FlatAndNoisyScanner(OrgTechUnit):
    def __init__(self):
        super().__init__(name='Scanner', size=1)

    def __call__(self):
        print(f'{self.name} can do "Z-z-z-z-z" very loudly. And scan.')


class BigWhiteXerox(OrgTechUnit):
    def __init__(self, price=800):
        super().__init__(name='Xerox', price=price, size=5)

    def __call__(self):
        print(f'{self.name} can do many copies. Also can scan & print butts. Instruction added.')
