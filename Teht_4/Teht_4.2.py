inches = 0
while inches >= 0:
    inches = float(input("Syötä tuumamäärä: "))
    if inches >= 0:
        centimeters = float(inches) * 2.54
        print(f"{inches} tuumaa on {centimeters:.2f} senttimetriä.")
    else:
        quit()