class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = 0
        self.tamanhetkinen_nopeus = 0
    pass


##luo uusi auto
auto = Auto("ABC-123", 142)

print(auto.huippunopeus, auto.rekisteritunnus, auto.kuljettu_matka, auto.tamanhetkinen_nopeus)