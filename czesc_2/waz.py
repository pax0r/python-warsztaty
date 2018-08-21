import random


class Punkt(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def losuj_punkt(cls, max_x, max_y):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        return cls(x, y)


class Waz(Punkt):
    def znak(self, liczba):
        if liczba < 0:
            return -1
        if liczba > 0:
            return 1
        return 0

    def zrob_krok(self, cel):
        roznica_x = self.x - cel.x
        roznica_y = self.y - cel.y
        self.x -= self.znak(roznica_x)
        self.y -= self.znak(roznica_y)


if __name__ == '__main__':
    jedzonko = Punkt.losuj_punkt(500, 500)
    waz = Waz.losuj_punkt(500, 500)
    while waz.x != jedzonko.x or waz.y != jedzonko.y:
        waz.zrob_krok(jedzonko)
        print(waz.x, waz.y)
