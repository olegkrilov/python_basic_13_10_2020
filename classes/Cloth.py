class Cloth:

    __slots__ = ('__name', '__divider', '__additional_size', 'size', 'stature')

    def __init__(self, name):
        self.__name = name
        self.__divider = 1
        self.__additional_size = 0

    def __setitem__(self, key, value):
        try:
            self[key] = float(value)
        except ValueError:
            print('Should be a Number')

    @property
    def tissue_consumption(self):
        __size = 0

        if hasattr(self, 'size'):
            __size += self.size
        elif hasattr(self, 'stature'):
            __size += self.stature

        return round(__size / (self.__divider or 1) + self.__additional_size, 2)

    @property
    def name(self):
        return self.__name

    @property
    def divider(self):
        return self.__divider

    @divider.setter
    def divider(self, value):
        try:
            self.__divider = float(value)
        except ValueError:
            print('Should be a Number')

    @property
    def additional_size(self):
        return self.__divider

    @additional_size.setter
    def additional_size(self, value):
        try:
            self.__additional_size = float(value)
        except ValueError:
            print('Should be a Number')


class Coat(Cloth):

    def __init__(self, size):
        super().__init__('Coat')
        self.size = size
        self.divider = 6.5
        self.additional_size = .5


class Suit(Cloth):

    def __init__(self, stature):
        super().__init__('Suit')
        self.stature = stature
        self.divider = .5
        self.additional_size = .3
