lentoasemat = {}

while True:
    valinta = input("Valitse toiminto (uusi, haku, lopeta): ")

    if valinta == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "haku":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "lopeta":
        break