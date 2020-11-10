from controllers.AbstractTask import AbstractTask
from classes.OutstandingOrgTechStorage import (
    OutstandingOrgTechStorage,
    AmazingOrgTechMarket
)
from common.utils import (
    clear_screen
)


class Task4(AbstractTask):

    def __init__(self):
        super().__init__()
        self.Storage = OutstandingOrgTechStorage()
        self.Market = AmazingOrgTechMarket()

    def __request_for_action(self):
        _cycle = True

        clear_screen()
        print(self.Storage)
        print(self.Market)

        while _cycle:
            print('\nInput your directive\n[Show Info] for details:')
            res = self.Market(input('>>> '))

            if isinstance(res, str):
                print(res)
            elif isinstance(res, dict):
                close_deal = False

                if res['deal'] == 'buy':
                    close_deal = self.Storage - res
                elif res['deal'] == 'sell':
                    close_deal = self.Storage + res

                if close_deal:
                    self.Market.close_deal(res)
                    _cycle = False

    def run(self):
        self.__request_for_action()
