
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


# Pääohjelma
sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

# Asetetaan nopeudet
sähköauto.kiihdytä(120)
polttomoottoriauto.kiihdytä(100)

# Ajetaan kolme tuntia
sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

# Tulostetaan matkamittarilukemat
print(f"Sähköauto {sähköauto.rekisteritunnus}: {sähköauto.kuljettu_matka} km")
print(f"Polttomoottoriauto {polttomoottoriauto.rekisteritunnus}: {polttomoottoriauto.kuljettu_matka} km")
