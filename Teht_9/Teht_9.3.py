class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = 0
        self.nopeus = 0
    pass

    def kiihdyta(self, kmh):
        if self.nopeus + kmh > self.huippunopeus:
            self.nopeus = self.huippunopeus

        else:
            self.nopeus += kmh

        if self.nopeus < 0:
            self.nopeus = 0
    pass

    def kulje(self, tunti):
        self.kuljettu_matka += self.nopeus * tunti


##luo uusi auto
auto = Auto("ABC-123", 142)

print(auto.huippunopeus, auto.rekisteritunnus, auto.kuljettu_matka, auto.nopeus)

Auto.kiihdyta(auto, 60)

print(auto.nopeus)

Auto.kulje(auto, 1.5)

print(auto.kuljettu_matka)
