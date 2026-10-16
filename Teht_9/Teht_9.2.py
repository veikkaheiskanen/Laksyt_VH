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


##luo uusi auto
auto = Auto("ABC-123", 142)

print(auto.huippunopeus, auto.rekisteritunnus, auto.kuljettu_matka, auto.nopeus)

ekakiihdytys = 30
tokakiihdytys = 70
kolmaskiihdytys = 50

Auto.kiihdyta(auto, ekakiihdytys)
Auto.kiihdyta(auto, tokakiihdytys)
Auto.kiihdyta(auto, kolmaskiihdytys)

print(auto.nopeus)

Auto.kiihdyta(auto, -200)

print(auto.nopeus)


