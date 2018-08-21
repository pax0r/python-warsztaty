class Samochod(object):
    def __init__(self, marka, kolor):
        self.marka = marka
        self.kolor = kolor
        self.predkosc = 0

    def przyspiesz(self):
        self.predkosc += 1
        # self.predkosc = self.predkosc + 1

    def zwolnij(self):
        self.predkosc -= 1


autko = Samochod("BMW", "Czerwony")
autko2 = Samochod("Fiat 126p", "Pomaranczowy")
print(autko.kolor, autko.marka, autko.predkosc)
autko.przyspiesz()
print(autko.predkosc)
autko.przyspiesz()
print(autko.predkosc)
print(autko2.kolor, autko2.marka, autko2.predkosc)
autko.zwolnij()
print(autko.predkosc)
