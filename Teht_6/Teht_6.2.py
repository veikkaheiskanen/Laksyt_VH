import random

def noppa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan maksimisilmäluku: "))

while True:
    silmaluku = noppa(maksimi)
    print(silmaluku)

    if silmaluku == maksimi:
        break