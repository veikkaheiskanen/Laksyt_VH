import random


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi}")
        print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<18}{'Nopeus':<12}{'Kuljettu matka'}")
        print("-" * 65)

        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<18}{auto.huippunopeus:<18}{auto.nopeus:<12}{auto.kuljettu_matka}")

    def kilpailu_ohi(self):
        return any(auto.kuljettu_matka >= self.pituus for auto in self.autot)


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = 0
        self.nopeus = 0

    def kiihdyta(self, kmh):
        if self.nopeus + kmh > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += kmh

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti):
        self.kuljettu_matka += self.nopeus * tunti


# Luodaan 10 autoa ja lisätään ne listaan
autot = []

for uusi_auto in range(1, 11):
    rekisteritunnus = "ABC-" + str(uusi_auto)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))


# Luodaan kilpailu
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

# Aloitetaan kilpailu
tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    # Tulostetaan tilanne 10 tunnin välein
    if tunnit % 10 == 0 and not kilpailu.kilpailu_ohi():
        print(f"\nKilpailua kulunut {tunnit} tuntia")
        kilpailu.tulosta_tilanne()


# Tulostetaan lopputilanne
print(f"\nKilpailu päättyi {tunnit} tunnin jälkeen!")
kilpailu.tulosta_tilanne()