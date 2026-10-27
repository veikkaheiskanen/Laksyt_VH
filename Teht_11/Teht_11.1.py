class Julkaisu:

    def init(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")


class Lehti(Julkaisu):

    def init(self, nimi, päätoimittaja):
        super().init(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")


class Kirja(Julkaisu):

    def init(self, nimi, kirjoittaja, sivumäärä):
        super().init(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")


lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Likson", 200)

lehti.tulosta_tiedot()
print()
kirja.tulosta_tiedot()