class Talo:
    def __init__(self, max_kerros, min_kerros, hissien_maara):
        self.max_kerros = max_kerros
        self.min_kerros = min_kerros
        self.hissien_maara = hissien_maara
        self.hissin_nro = [
            Hissi(max_kerros, min_kerros)
            for _ in range(self.hissien_maara)
        ]

    def aja_hissia(self, hissin_nro, kerros):
        self.hissin_nro[hissin_nro].siirry_kerrokseen(kerros)


class Hissi:
    def __init__(self, max_kerros, min_kerros):
        self.max_kerros = max_kerros
        self.min_kerros = min_kerros
        self.nyk_kerros = min_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros > self.max_kerros:
            kerros = self.max_kerros
        if kerros < self.min_kerros:
            kerros = self.min_kerros

        while kerros > self.nyk_kerros:
            self.kerros_ylös()

        while kerros < self.nyk_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        self.nyk_kerros += 1

    def kerros_alas(self):
        self.nyk_kerros -= 1


# Luodaan talo ja hissit
t = Talo(5, 0, 2)

# Ajetaan hissi 1 kerrokseen 3
t.aja_hissia(0, 3)

# Ajetaan hissi 2 kerrokseen 4
t.aja_hissia(1, 4)

# Tulostetaan hissien nykyiset kerrokset
print(f"Hissi 1 on kerroksessa: {t.hissin_nro[0].nyk_kerros}")
print(f"Hissi 2 on kerroksessa: {t.hissin_nro[1].nyk_kerros}")