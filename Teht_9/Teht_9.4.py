import random

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


# Luodaan 10 autoa ja lisätään ne listaan

autot = []

for uusi_auto in range(1, 11):
    rekisteritunnus = "ABC-" + str(uusi_auto)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

# Aloitetaan kisa
while any(auto.kuljettu_matka < 10000 for auto in autot):
    for auto in autot:
        Auto.kiihdyta(auto, random.randint(-10, 15))
        Auto.kulje(auto, 1)

# Tulostetaan jokaisen auton tiedot
for auto in autot:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus}, Kuljettu matka: {auto.kuljettu_matka}, Nopeus: {auto.nopeus}")





