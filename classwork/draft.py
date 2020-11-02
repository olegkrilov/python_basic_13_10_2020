from datetime import datetime

print('les 6')


class Car:

    _collection = {}

    __totally_secret = 'ASDASDASDASD'

    def __init__(self, engine, brand, production_date=None):
        self.brand = brand
        self.engine = engine
        self.production_date = production_date
        self._collection[self.brand] = self

    def run(self):
        print(f'Starting {self.engine} engine')
        _i = 10
        while _i:
            print('>' * (10 - _i))
            _i -= 1

        return self.hong()

    def hong(self):
        print(f'{self.__totally_secret} says: BI-BIP!!!!')

        return self


class FordPickUp(Car):
    def __init__(self, name, carrying):
        super().__init__(engine='v6.3', brand='Ford', production_date=datetime.now().year)
        self.name = name
        self.carrying = carrying


class Robot:
    def __init__(self, os):
        self.os = os

    def run(self):
        print(f'{self.os} says: BI-BI-BI-BU-BUP')


class Transformer(FordPickUp, Robot):
    def __init__(self, name):
        FordPickUp.__init__(self, name, 10000)
        Robot.__init__(self, 'WindowsXXl')


trans = Transformer('Vasisualy')

trans.run()



# pickup = FordPickUp('Raptor', 2000).run().hong().hong().hong()



#
# ford_t = Car('v1.6', 'Ford').run()
#
# chevrolet = Car('v1.8', 'Chevrolet')

# print(Car, ford_t, chevrolet)


