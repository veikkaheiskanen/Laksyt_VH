import random
summa = 0
silmäluku = 0
nopat = int(input("Syötä nopanheittojen määrä: "))

while nopat > 0:
    silmäluku = random.randint(1, 6)
    summa += silmäluku
    nopat -= 1

print(f"Noppien silmälukujen summa on: {summa}")


