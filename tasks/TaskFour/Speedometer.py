
class Speedometer:

    red_tile = '\33[91m' + u'\u2593' + '\033[0m'
    yellow_tile = '\33[93m' + u'\u2593' + '\033[0m'
    green_tile = '\33[92m' + u'\u2593' + '\033[0m'

    def show_speed(self, speed):
        print('Speed:')
        _tiles_len = speed // 3
        _tiles = ''
        _i = 0

        while _i <= _tiles_len:
            if 0 <= _i < 5:
                _tiles += self.green_tile
            elif 5 <= _i < 10:
                _tiles += self.yellow_tile
            else:
                _tiles += self.red_tile

            _i += 1

        print(_tiles)
