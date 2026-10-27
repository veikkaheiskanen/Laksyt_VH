class Hissi:
    def __init__(self):
        self.nyk_kerros = 0
        self.max_kerros = 5
        self.min_kerros = 0

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


h = Hissi()
print(h.nyk_kerros)

h.siirry_kerrokseen(5)
print(h.nyk_kerros)

h.siirry_kerrokseen(2)
print(h.nyk_kerros)