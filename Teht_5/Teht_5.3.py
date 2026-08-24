import math

value = float(input("Syötä luku: "))
alkuluku = False

if value <= 1:
    print(f"{value} ei ole alkuluku")
else:
    alkuluku = True

    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print(f"{value} on alkuluku")
    else:
        print(f"{value} ei ole alkuluku")